"""
    Description:

    Encontra objetos em lista

    Author:           @Palin/Renan
    Created:          2021-07-01
    Copyright:        (c) Ampere Consultoria Ltda
"""


def find_obj(lst_to_find, name_field: str, value_to_find):
    if len(lst_to_find) == 0:
        return None
    try:
        lst_result = list(
            filter(lambda x: getattr(x, name_field) == value_to_find, lst_to_find)
        )
        if len(lst_result) > 0:
            founded = lst_result[0]
        else:
            founded = None
    except IndexError as err:
        print(err)
    return founded


def find_obj_all(lst_to_find, name_field: str, value_to_find):
    """Ex:
    usinas = [
      {'cod_usina': "BAEDF8", 'nome': 'MACAUBAS'},
      {'cod_usina': "XEFZT", 'nome': 'SEABRA'},
    ]

      usina_found = list(filter(lambda usina: usina['cod_usina'] == 'BAEDF8', usinas))
      rateio_found = list(filter(lambda x: x['cod_barra'] == 'XXX', rateio))

      Args:
          lst_to_find ([type]): [description]
          name_field (str): [description]
          value_to_find ([type]): [description]

      Returns:
          [type]: [description]
    """
    if len(lst_to_find) == 0:
        return None
    try:
        lst_result = list(
            filter(lambda x: getattr(x, name_field) == value_to_find, lst_to_find)
        )
        if len(lst_result) > 0:
            founded = lst_result
        else:
            founded = None
    except IndexError as err:
        print(err)
    return founded
