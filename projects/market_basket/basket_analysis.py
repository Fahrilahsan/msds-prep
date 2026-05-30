import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from decorators import timer
from mlxtend.frequent_patterns import apriori, association_rules


class BasketAnalysis:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self._basket = None

    def __repr__(self) -> str:
        return f"BasketAnalysis(members={self.df['member_id'].nunique()}, classes={self.df['class_name'].nunique()})"

    def __len__(self) -> int:
        return self.df['member_id'].nunique()

    @classmethod
    def from_csv(cls, filepath: str) -> 'BasketAnalysis':
        df = pd.read_csv(filepath)
        return cls(df)

    @property
    def basket(self) -> pd.DataFrame:
        if self._basket is None:
            self._basket = self.df.groupby(['member_id', 'class_name']).size()\
                                  .unstack(fill_value=0)\
                                  .map(lambda x: 1 if x > 0 else 0)
        return self._basket

    @timer
    def get_rules(self, min_support: float = 0.01, min_threshold: float = 1.0) -> pd.DataFrame:
        frequent_itemsets = apriori(self.basket, min_support=min_support, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold)
        return rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]\
                    .sort_values(by=['confidence', 'lift'], ascending=False)

    def plot_network(self, rules: pd.DataFrame, filter_classes: list[str]) -> None:
        rules = rules.copy()
        rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
        rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

        filtered = rules[rules['antecedents'].isin(filter_classes)]

        G = nx.DiGraph()
        for _, row in filtered.iterrows():
            G.add_edge(row['antecedents'], row['consequents'], weight=row['lift'])

        pos = nx.spring_layout(G, k=0.5, seed=42)

        plt.figure(figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightblue',
                font_size=10, node_size=3000, font_weight='bold', edge_color='gray')

        edge_labels = {k: round(v, 2) for k, v in nx.get_edge_attributes(G, 'weight').items()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title(f"Association Rules Network: {', '.join(filter_classes)}")
        plt.show()


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    basket = BasketAnalysis.from_csv(os.path.join(BASE_DIR, 'cohort_masked.csv'))
    rules = basket.get_rules()
    basket.plot_network(rules, ['BODYPUMP'])