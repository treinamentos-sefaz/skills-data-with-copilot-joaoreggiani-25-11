"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    fig, ax = plt.subplots()
    sns.histplot(data=df, x="rating", bins=20, ax=ax)
    ax.set(title="Distribuição das Avaliações dos Vinhos",
           xlabel="Avaliação (Rating)", ylabel="Frequência")
    fig.savefig(out_path, format="png", dpi=150)
    plt.close(fig)


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    counts = df["variety"].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=counts.values, y=counts.index, ax=ax)
    ax.set(title="Top 10 Variedades de Vinhos",
           xlabel="Quantidade de Vinhos", ylabel="Variedade")
    fig.tight_layout()
    fig.savefig(out_path, format="png", dpi=150)
    plt.close(fig)


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    top_varieties = df["variety"].value_counts().head(5).index
    filtered_df = df[df["variety"].isin(top_varieties)]

    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_df, x="variety", y="rating", ax=ax)
    ax.set(title="Distribuição das Avaliações por Variedade",
           xlabel="Variedade", ylabel="Avaliação (Rating)")
    fig.tight_layout()
    fig.savefig(out_path, format="png", dpi=150)
    plt.close(fig)
