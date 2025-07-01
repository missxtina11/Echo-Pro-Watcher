# utils/chart_utils.py
import matplotlib.pyplot as plt
import os

def plot_pie_chart(wallet):
    labels = ['XRP', 'STB']
    sizes = [30, 70]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    path = f"/mnt/data/{wallet}_pie.png"
    plt.savefig(path)
    return path

def plot_holder_distribution():
    holders = ['Top 1', 'Top 2', 'Others']
    shares = [25, 15, 60]
    fig, ax = plt.subplots()
    ax.pie(shares, labels=holders, autopct='%1.1f%%')
    path = "/mnt/data/holders_chart.png"
    plt.savefig(path)
    return path
