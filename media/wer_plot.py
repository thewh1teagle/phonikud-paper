"""
uv pip install matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Data for the models
models = [
    ("Piper - Medium", 0.231, 0.09, "Ours"),
    ("Piper - High", 0.213, 0.13, "Ours"),
    ("StyleTTS2", 0.188, 0.50, "Ours"),
    ("MMS", 0.520, 0.21, "Open"),
    ("SASPEECH", 0.374, 0.16, "Open"),
    ("RoboShaul", 0.245, 1.58, "Open"),
    ("Gemini", 0.155, 1.22, "Proprietary"),
    ("OpenAI", 0.187, 1.60, "Proprietary"),
]

# Filter out models with None values for WER or RTF
filtered = [m for m in models if m[1] is not None and m[2] is not None]

# Create the figure and axes with better sizing
fig, ax = plt.subplots(figsize=(12, 8))

# Color mapping with fancy colors
colors = {'Ours': '#e74c3c', 'Open': '#3498db', 'Proprietary': '#f39c12'}
legend_elements = []

# Plot each model
for name, wer, rtf, category in filtered:
    # Determine color based on category
    color = colors[category]
    
    # Determine size and weight for our models
    size = 180  # Same size for all models
    weight = 'bold' if category == 'Ours' else 'normal'
    edgewidth = 2 if category == 'Ours' else 1.5

    # Create label for the point
    label = f"Ours ({name})" if category == 'Ours' else name

    # Plot the scatter point
    scatter = ax.scatter(rtf, wer, s=size, c=color, edgecolors='black', 
                        linewidths=edgewidth, zorder=3, alpha=0.8)

    # Adjust text position for each model
    if name == "Piper - Medium":
        x_text = rtf * 0.88
        y_text = wer + 0.016
        ha = 'left'
        va = 'bottom'
    elif name == "Piper - High":
        x_text = rtf * 1.08
        y_text = wer
        ha = 'left'
        va = 'center'
    elif name == "Gemini":
        x_text = rtf
        y_text = wer - 0.008
        ha = 'center'
        va = 'top'
    elif name == "HebTTS":  
        x_text = rtf * 0.75
        y_text = wer
        ha = 'right'
        va = 'center'
    elif name == "Google":
        x_text = rtf * 0.8
        y_text = wer - 0.010
        ha = 'left'
        va = 'center'
    elif name == 'LoTHM':
        x_text = rtf * 0.85
        y_text = wer
        ha = 'right'
        va = 'center'
    elif name == "OpenAI":
        x_text = rtf
        y_text = wer - 0.008
        ha = 'center'
        va = 'top'
    elif name == "RoboShaul":
        x_text = rtf
        y_text = wer + 0.012
        ha = 'center'
        va = 'bottom'
    elif name == "Piper":
        x_text = rtf * 0.9
        y_text = wer  - 0.010
        ha = 'left'
        va = 'top'
    elif name == "StyleTTS2":
        x_text = rtf * 0.8
        y_text = wer - 0.018
        ha = 'center'
        va = 'top'
    elif name == "SASPEECH":
        x_text = rtf + 0.02
        y_text = wer - 0.000
        ha = 'left'
        va = 'center'
    elif name == "MMS":
        x_text = rtf
        y_text = wer + 0.008
        ha = 'center'
        va = 'bottom'
    else:
        x_text = rtf * 1.15
        y_text = wer
        ha = 'left'
        va = 'center'

    # Add text label for each point
    fontsize = 20 if category == 'Ours' else 22
    ax.text(x_text, y_text, label, fontsize=fontsize, ha=ha, va=va, 
            color='black', weight=weight, zorder=4)

ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, subs=(1.0, 2.0, 5.0), numticks=10))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.1f}"))

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f"{y:.2f}"))

# Increase tick label font sizes
ax.tick_params(axis='both', which='major', labelsize=18)

# Set axis labels with larger font
ax.set_xlabel("← RTF (Faster)", fontsize=24, fontweight='bold')
ax.set_ylabel("← WER (Precise)", fontsize=24, fontweight='bold')

# Add subtle grid
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Extend x-axis limits by 30% to make space for labels
x_min, x_max = ax.get_xlim()
ax.set_xlim(x_min, x_max * 1.3)

# Extend y-axis limits slightly for better spacing
y_min, y_max = ax.get_ylim()
ax.set_ylim(y_min - 0.01, y_max + 0.02)

# ADD REAL-TIME THRESHOLD LINE AT RTF = 1.0
# Get the current axis limits
y_min, y_max = ax.get_ylim()
x_min, x_max = ax.get_xlim()

# Draw vertical dashed line at RTF = 1.0 from top to bottom
ax.axvline(x=1.0, color="#000000", linestyle='--', linewidth=3, alpha=0.8, zorder=5)

# Position text near the dashed line at the top (left side of the line)
text_x = 0.95  # Slightly to the left of the line
text_y = y_max - (y_max - y_min) * 0.05  # Near the top
text_label = ax.text(text_x, text_y, 'Real-Time\n(RTF ≤ 1.0)', 
                     fontsize=16, fontweight='bold', ha='right', va='top', 
                     color="#000000", zorder=6)

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Save with high quality
plt.savefig("wer_plot.png", dpi=300, bbox_inches='tight', facecolor='white')
plt.show()