import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

def generate_graph():
    # Set style
    sns.set_theme(style="whitegrid")
    
    # Create data
    np.random.seed(42)
    normal_data = np.random.normal(loc=50, scale=10, size=1000)
    skewed_data = np.random.exponential(scale=20, size=1000)
    
    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Normal Distribution
    sns.histplot(normal_data, kde=True, ax=axes[0], color='skyblue', element="step")
    axes[0].set_title("Normal Distribution (Symmetrical)", fontsize=14, fontweight='bold')
    axes[0].set_xlabel("Value")
    axes[0].set_ylabel("Frequency")
    # Add annotation
    axes[0].text(0.5, 0.9, "Strategy: MEAN", transform=axes[0].transAxes, 
                 ha="center", fontsize=12, bbox=dict(facecolor='white', alpha=0.8, edgecolor='blue'))
    
    # Plot 2: Skewed Distribution
    sns.histplot(skewed_data, kde=True, ax=axes[1], color='salmon', element="step")
    axes[1].set_title("Skewed Distribution (Asymmetrical)", fontsize=14, fontweight='bold')
    axes[1].set_xlabel("Value")
    axes[1].set_ylabel("Frequency")
    # Add annotation
    axes[1].text(0.5, 0.9, "Strategy: MEDIAN", transform=axes[1].transAxes, 
                 ha="center", fontsize=12, bbox=dict(facecolor='white', alpha=0.8, edgecolor='red'))
    
    plt.tight_layout()
    
    # Save
    output_path = os.path.join("docs", "images", "distribution_logic.png")
    plt.savefig(output_path, dpi=300)
    print(f"Graph saved to {output_path}")

if __name__ == "__main__":
    generate_graph()
