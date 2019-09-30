import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.express as px
import os

gapminder = plotly.data.gapminder()
btm = html.Div([
    dcc.Link("メニューに戻る", href="/")
], style={"textAlign": "center"})

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

server = app.server

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div([
        html.P("Dash-Samples-Test", style={"fontSize": 30,
                                           "textAlign": "center", "color": "lime"})
    ]),
    html.Div(id="page-contents"),
], style={"width": "85%", "margin": "auto"})

index_page = html.Div([
    html.Div([
        dcc.Link("Dash入門 - DashのグラフにPlotlyを利用する - 散布図のアニメーション",
                 href="/scatter-animation", style={"textDecoration": "none"})], style={"margin": 30}),
    html.Br(),
    html.Div([
        dcc.Link("Dash入門 - DashのグラフにPlotlyを利用する - 階級区分図のアニメーション",
                 href="/choropleth-animation", style={"textDecoration": "none"})], style={"margin": 30}),
], style={"textAlign": "center"})

scatter_animation = html.Div([
    html.P("散布図のアニメーション", style={"fontSize": 30, "textAlign": "center"}),
    html.P("左下のアニメーションボタンを押すと動きます。", style={
           "fontSize": 30, "textAlign": "center"}),
    dcc.Graph(
        figure=px.scatter(gapminder, x="gdpPercap",
                          y="lifeExp", size="pop", color="continent", hover_name="country", animation_frame="year", log_x=True,  size_max=45, range_x=[100, 100000], range_y=[25, 90], title="1人当たりGDP（x軸）と平均寿命（y軸）のグラフ")
    ),
    btm
])

choropleth_animation = html.Div([
    html.P("階級区分図のアニメーション", style={"fontSize": 30, "textAlign": "center"}),
    html.P("左下のアニメーションボタンを押すと動きます。", style={
           "fontSize": 30, "textAlign": "center"}),
    dcc.Graph(figure=px.choropleth(gapminder, locations="iso_alpha", color="lifeExp",
                                   hover_name="country", animation_frame="year", range_color=[20, 80])),
    btm
])

@app.callback(dash.dependencies.Output("page-contents", "children"),
              [dash.dependencies.Input("url", "pathname")])
def update_contents(pathname):
    if pathname == "/scatter-animation":
        return scatter_animation
    elif pathname == "/choropleth-animation":
        return choropleth_animation
    else:
        return index_page


if __name__ == "__main__":
    app.run_server(debug=True)
