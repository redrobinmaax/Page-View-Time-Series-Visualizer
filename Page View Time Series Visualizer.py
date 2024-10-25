#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load and Clean Data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data by removing the top and bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Step 2: Line Plot
def draw_line_plot():
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot the data
    ax.plot(df.index, df['value'], color='red')
    
    # Set the title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save the figure and return it
    fig.savefig('line_plot.png')
    return fig

# Step 3: Bar Plot
def draw_bar_plot():
    # Copy the data and add 'year' and 'month' columns
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Pivot table for average monthly views per year
    df_bar = df_bar.groupby(['year', 'month']).mean().unstack()

    # Create the figure and axis
    fig = df_bar.plot(kind='bar', figsize=(12, 6)).figure
    
    # Set the labels and title
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Monthly Average Page Views per Year')
    plt.legend(title='Months', labels=df_bar.columns.levels[1])

    # Save the figure and return it
    fig.savefig('bar_plot.png')
    return fig

# Step 4: Box Plot
def draw_box_plot():
    # Prepare the data for box plots
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')

    # Sort months in calendar order
    df_box['month'] = pd.Categorical(df_box['month'], categories=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)

    # Create the figure and axes
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save the figure and return it
    fig.savefig('box_plot.png')
    return fig

