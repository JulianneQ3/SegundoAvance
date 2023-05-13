import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math
import time

#import fronted
from fronted.main import layout

#import backend
from backend.cartaplasticidad import cartaPlasticidad

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout



#desarrollamos la tabla de tamices
@app.callback(
    Output('salidaTablaTamices', 'children'),
    Input('porcentajePasa', 'value'),
    Input('Diámetro (mm)', 'value')
)

def tablaTamices(salidaTablaTamices, porcentajePasa):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image, messages = curva_granulometrica(salidaTablaTamices, porcentajePasa)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    messages_element = html.Label(messages)

    return html.Div([image_element, messages_element])




#calculamos la curva granulométrica
@app.callback(
    Output('salidaCurvaGranulometrica', 'children'),
    Input('Porcentaje pasa acumulado (%)', 'value'),
    Input('Diámetro (mm)', 'value')
)

def curva_granulometrica(abertura, pasa, tamiz):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image, messages = curva_granulometrica(abertura, pasa, tamiz)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    messages_element = html.Label(messages)

    return html.Div([image_element, messages_element])





#calculamos la carta de plasticidad
@app.callback(
    Output('salidaCartaPlasticidad', 'children'),
    Input('Limite_liquido', 'value'),
    Input('Indice_plasticidad', 'value')
)

def cartaPlasticidadDash(Limite_liquido, Indice_plasticidad):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image, messages = cartaPlasticidad(Limite_liquido, Indice_plasticidad)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    messages_element = html.Label(messages)

    return html.Div([image_element, messages_element])


if __name__ == '__main__':
    app.run_server(debug=True)
