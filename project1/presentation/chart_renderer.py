"""
File: chart_renderer.py
Course: CST8002 - Practical Project Part 4
Author: Yi Wu (040787698)

Purpose:
    Presentation layer component for rendering a Vertical Bar Chart
    using matplotlib. This module does not know about CSV files or
    business rules; it only receives prepared labels and numeric values.
"""

from typing import List
import matplotlib.pyplot as plt


class ChartRenderer:
    """
    Renders a vertical bar chart based on prepared labels and values.
    """

    def show_vertical_bar_chart(
        self,
        labels: List[str],
        values: List[float],
        title: str,
        x_label: str,
        y_label: str,
    ) -> None:
        """
        Display a vertical bar chart. If there is no data, a message is printed
        instead of attempting to draw an empty chart.
        """
        if not values:
            print("No numeric data available to display a chart.")
            return

        plt.figure()
        plt.bar(labels, values)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
