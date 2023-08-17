import pandas as pd
import plotly.express as px


def plot_multi_series(
    data, x_label, y_labels, colors, title, template, normalize=False
):
    df = pd.DataFrame(data)
    if normalize:
        for label in y_labels:
            df[label] = df[label] * 100 / df[label].sum()
        title += " (Normalized)"
    fig = px.bar(
        data_frame=df,
        x=x_label,
        y=y_labels,
        opacity=0.9,
        orientation="v",
        barmode="group",
        title=title,
        color_discrete_sequence=colors,
        template=template,
    )
    if normalize:
        fig.update_layout(yaxis_ticksuffix="%")

    fig.update_layout(legend={"title_text": ""})
    fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.7, traceorder= 'reversed'))
    
    fig.show()


def plot_multi_series_horizontal(
    data, x_labels, y_label, colors, title, template, normalize=False
):
    df = pd.DataFrame(data)
    if normalize:
        for label in x_labels:
            df[label] = df[label] * 100 / df[label].sum()
        title += " (Normalized)"
    fig = px.bar(
        data_frame=df,
        x=x_labels,
        y=y_label,
        orientation="h",
        barmode="group",
        color_discrete_sequence=colors,
        template=template,
    )

    if normalize:
        fig.update_layout(xaxis_ticksuffix="%")

    fig.update_layout(legend={"title_text": ""})
    fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.7, traceorder= 'reversed'))
    fig.show()


def plot_multi_series_stacked(
    data, x_label, y_labels, colors, title, template, normalize=False
):
    df = pd.DataFrame(data)
    if normalize:
        for label in y_labels:
            df[label] = df[label] * 100 / df[label].sum()
        title += " (Normalized)"
    fig = px.bar(
        data_frame=df,
        x=x_label,
        y=y_labels,
        opacity=0.9,
        orientation="v",
        barmode="relative",
        title=title,
        color_discrete_sequence=colors,
        template=template,
    )
    if normalize:
        fig.update_layout(yaxis_ticksuffix="%")
    fig.update_layout(legend={"title_text": ""})
    fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.7, traceorder= 'reversed'))
    fig.show()


def plot_multi_series_stacked_horizontal(
    data, x_labels, y_label, colors, title, template, normalize=False
):
    df = pd.DataFrame(data)
    # if normalize:
    #     df = df.div(df.sum(axis=1), axis=0)
    #     title += " (Normalized)"
    if normalize:
        for label in x_labels:
            df[label] = df[label] * 100 / df[label].sum()
        title += " (Normalized)"
    fig = px.bar(
        data_frame=df,
        x=x_labels,
        y=y_label,
        orientation="h",
        barmode="relative",
        color_discrete_sequence=colors,
        template=template,
    )
    fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.7, traceorder= 'reversed'))

    fig.show()

