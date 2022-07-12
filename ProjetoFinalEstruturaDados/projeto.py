values_permited = ['M', 'G', 'C']  # motocicletas , carros grandes e carros comuns
from PySimpleGUI import PySimpleGUI as s


class User:
    def __init__(self, name, phone, typecaruser):
        self._name = name
        self._phone = phone
        self._typecar = typecaruser


class SystemParking:
    def __init__(self):
        self._blocked = False
        self._list_spaces_automobile = []
        self._available_quantity_motorcycles = 0
        self._available_quantity_common_cars = 0
        self._available_quantity_big_cars = 0
        self._number_mototcycles_not_sparking = 0
        self._number_common_cars_not_sparking = 0
        self._number_big_cars_not_sparking = 0

    def return_number_mototcycles_not_sparking(self):
        return self._number_mototcycles_not_sparking

    def return_number_common_cars_not_sparking(self):
        return self._number_common_cars_not_sparking

    def return_number_big_cars_not_sparking(self):
        return self._number_big_cars_not_sparking

    def add_not_sparking(self, type):
        if type == "M":
            self._number_mototcycles_not_sparking += 1
        elif type == "G":
            self._number_big_cars_not_sparking += 1
        else:
            self._number_common_cars_not_sparking += 1

    def return_situation_now_system_parking(self):
        return f'''
        Quantidade de vagas de MOTOS disponíves : {self._available_quantity_motorcycles}
        Quantidade de vagas de CARROS COMUNS disponíveis : {self._available_quantity_common_cars}
        Quantidade de vagas de CARROS GRANDES disponíveis : {self._available_quantity_big_cars}'''

    def return_quantity_spaces_available_motorcycles(self):
        return self._available_quantity_motorcycles

    def return_quantity_spaces_common_cars(self):
        return self._available_quantity_common_cars

    def return_quantity_spaces_big_cars(self):
        return self._available_quantity_big_cars

    def return_list_spaces_automobile(self):
        return self._list_spaces_automobile

    def update_available_quantity_vehicules(self, type, signal):
        if self._available_quantity_motorcycles != 0:
            if signal == "+":
                if type == "M":
                    self._available_quantity_motorcycles += 1
                elif type == "C":
                    self._available_quantity_common_cars += 1
                else:
                    self._available_quantity_big_cars += 1
            else:
                if type == "M":
                    self._available_quantity_motorcycles -= 1
                elif type == "C":
                    self._available_quantity_common_cars -= 1
                else:
                    self._available_quantity_big_cars -= 1

    def __len__(self):
        return len(self._list_spaces_automobile)

    def __str__(self):
        return self._list_spaces_automobile.__str__()

    def insert_list_spaces_automobile(self, space):
        if space._type == "M":
            self._available_quantity_motorcycles += 1
        elif space._type == "G":
            self._available_quantity_big_cars += 1
        else:
            self._available_quantity_common_cars += 1
        self._list_spaces_automobile.append(space)

    def park(self, type):
        for space in self._list_spaces_automobile:
            if (space._type == type and space._free == True):
                self.update_available_quantity_vehicules(type, "-")
                print("Obrigado, pf estacione na vaga de número !", space._id)
                space._free = False
                return True, space._id
        self.add_not_sparking(type)
        print("Não foi possível estacionar pois está cheio")
        return False, 0

    def exit(self, index):
        for space in self._list_spaces_automobile:
            if (space._id == index and space._free == False):
                space._free = True
                self.update_available_quantity_vehicules(space._type, "+")
                print("Obrigado, por utilizar nosso serviços, volte sempre !")
                return True
        print("Não foi possível liberar a vaga pois ela já está vazia !")
        print("exit")

    def report(self):
        return self._number_mototcycles_not_sparking, self._number_common_cars_not_sparking, self._number_big_cars_not_sparking


class Automobile:
    def __init__(self, board, free, type):
        self._board = board  # placa do carro
        self._free = free
        self._type = type
        if type is not values_permited:
            raise NameError("the values for the attribute 'type' must be \"M\",\"G\",\"C\"")


class SpacesAutomobile:
    def __init__(self, id, free, type):
        if (not type in values_permited):
            raise NameError("the values for the attribute 'type' must be \"M\",\"G\",\"C\"")
        self._id = id
        self._free = free  # se esta livre ou nao
        self._type = type

    def __str__(self):
        return f'Nome: {self._id} - Livre ?: {self._free} -  tipo da vaga : {self._type} '


class TelaPython:
    def __init__(self):
        self._blocked = False
        self._font1 = ("Roboto", 10)
        self._font2 = ("Roboto", 20)
        self._font3 = ("Roboto", 10, "bold")
        self._buttoncolor = "#00C703"
        self._buttoncolor3 = "#FFC703"
        self._size = (80, 3)
        self._size_input = (80, 20)

    def init_window(self, qtdm, qtdc, qtdg):
        layout = [
            [s.Text("Total de Vagas disponíveis", font=self._font2, background_color="#257A26"),
             s.Sizer(h_pixels=400, v_pixels=0),
             s.Button("Ver relatório", size=(70, 3), font=self._font1, button_color=self._buttoncolor3)],
            [s.Sizer(h_pixels=0, v_pixels=100)],
            [s.Button(str(qtdm) + " motocicletas", size=self._size, font=self._font1, button_color=self._buttoncolor),
             s.Button(str(qtdc) + " carros comuns", size=self._size, font=self._font1, button_color=self._buttoncolor)],
            [[s.Sizer(h_pixels=20, v_pixels=10)]],
            [s.Sizer(h_pixels=300, v_pixels=20),
             s.Button(str(qtdg) + " carros grandes", size=self._size, font=self._font1,
                      button_color=self._buttoncolor)],
            [[s.Sizer(h_pixels=20, v_pixels=100)]],
            [s.Sizer(h_pixels=100, v_pixels=0),
             s.Button("Estacionar", size=(70, 3), font=self._font1, button_color=self._buttoncolor3),
             s.Button("Tirar veículo", size=(70, 3), font=self._font1, button_color=self._buttoncolor)],
        ]

        return s.Window("Dados do Usuário", background_color="#257A26", finalize=True, layout=layout)

    def report_window(self, big_car, commom_car, motorcycle):
        layout = [
            ['', motorcycle, big_car, commom_car],
        ]
        heading = ['Quantidade', 'Motocicletas', 'Carros Grandes', 'Carros Comuns']

        layout = [
            [s.Text("Relatório de veículos que não conseguiram estacionar.", font=self._font2,
                    background_color="#257A26")],
            [s.Sizer(h_pixels=0, v_pixels=100)],
            [s.Table(values=layout, headings=heading, max_col_width=35,
                     auto_size_columns=True,
                     display_row_numbers=True,
                     justification='right',
                     num_rows=10,
                     key='-TABLE-',
                     row_height=35)],
            [s.Sizer(h_pixels=10, v_pixels=0),
             s.Button("Voltar", size=self._size, font=self._font1, button_color=self._buttoncolor3)]
        ]

        return s.Window("Relatório", background_color="#257A26", finalize=True, layout=layout)

    def window_park(self):
        layout = [
            [s.Text("Qual seu tipo de veículo ? Toque no tipo por favor ! ", font=self._font2,
                    background_color="#257A26")],
            [s.Sizer(h_pixels=0, v_pixels=100)],
            [s.Button("MOTOCICLETA", size=self._size, font=self._font1, button_color=self._buttoncolor),
             s.Button("CARRO COMUM", size=self._size, font=self._font1, button_color=self._buttoncolor)],
            [[s.Sizer(h_pixels=20, v_pixels=10)]],
            [s.Sizer(h_pixels=300, v_pixels=20),
             s.Button("CARRO GRANDE", size=self._size, font=self._font1, button_color=self._buttoncolor)],
            [[s.Sizer(h_pixels=20, v_pixels=100)]],
            [s.Sizer(h_pixels=100, v_pixels=0)],
            [[s.Sizer(h_pixels=300, v_pixels=0),
              s.Button("Voltar", size=self._size, font=self._font1, button_color=self._buttoncolor3)]]
        ]

        return s.Window("Escolhendo veículo", background_color="#257A26", finalize=True, layout=layout)

    def window_check(self, numero):
        layout = [
            [s.Text("Obrigado, em baixo está o número de sua vaga !", font=self._font2, background_color="#257A26")],
            [s.Sizer(h_pixels=0, v_pixels=50)],
            [s.Sizer(h_pixels=10, v_pixels=0),
             s.Button("Vaga de número " + str(numero), size=self._size, font=self._font1,
                      button_color=self._buttoncolor)],
            [s.Sizer(h_pixels=0, v_pixels=50)],
            [s.Sizer(h_pixels=0), s.Sizer(h_pixels=10, v_pixels=50),
             s.Button("Sair", size=self._size, font=self._font1, button_color=self._buttoncolor3)]
        ]

        return s.Window("Deu certo", background_color="#257A26", finalize=True, layout=layout)

    def window_exit(self):
        layout = [
            [s.Text("Digite o número da sua vaga para podermos liberar a cancela !", font=self._font2,
                    background_color="#257A26")],
            [s.Input(size=self._size_input, key='id')],
            [s.Sizer(h_pixels=0, v_pixels=50)],
            [s.Sizer(h_pixels=0), s.Sizer(h_pixels=10, v_pixels=50),
             s.Button("Confirmar", size=self._size, font=self._font1, button_color=self._buttoncolor3)]
        ]

        return s.Window("Sair", background_color="#257A26", finalize=True, layout=layout)

    def iniciar(self, system):
        qtdm = system.return_quantity_spaces_available_motorcycles()
        qtdc = system.return_quantity_spaces_common_cars()
        qtdg = system.return_quantity_spaces_big_cars()

        janela1, janela2, janela3, janela4, janela5 = self.init_window(qtdm, qtdc, qtdg), None, None, None, None

        while True:
            window, event, values = s.read_all_windows()
            if window == janela1 and event == s.WINDOW_CLOSED:
                break
            if window == janela1 and event == 'Estacionar':
                janela1.hide()
                janela2 = self.window_park()
            if window == janela1 and event == 'Tirar veículo':
                janela1.hide()
                janela4 = self.window_exit()
            if window == janela2 and event == 'Voltar':
                janela2.hide()
                janela1.un_hide()
            if window == janela2 and event == 'MOTOCICLETA' and self._blocked == False:
                self._blocked = True
                result, id = system.park("M")
                if result:
                    self._blocked = False
                    janela2.hide()
                    janela3 = self.window_check(id)
                else:
                    self._blocked = False
                    s.popup('Vagas para motocicletas estão lotadas !')
            if window == janela2 and event == 'CARRO COMUM' and self._blocked == False:
                self._blocked = True
                result, id = system.park("C")
                if result:
                    self._blocked = False
                    janela2.hide()
                    janela3 = self.window_check(id)
                else:
                    self._blocked = False
                    s.popup('Vagas para carro comum estão lotadas !')
            if window == janela2 and event == 'CARRO GRANDE' and self._blocked == False:
                self._blocked = True
                result, id = system.park("G")
                if result:
                    self._blocked = False
                    janela2.hide()
                    janela3 = self.window_check(id)
                else:
                    self._blocked = False
                    s.popup('Vagas para carro grande estão lotadas !')
            if window == janela3 and event == 'Sair':
                qtdm = system.return_quantity_spaces_available_motorcycles()
                qtdc = system.return_quantity_spaces_common_cars()
                qtdg = system.return_quantity_spaces_big_cars()
                janela3.hide()
                janela1 = self.init_window(qtdm, qtdc, qtdg)
            if window == janela4 and event == 'Confirmar':
                numerovaga = int(values["id"])
                system.exit(numerovaga)
                qtdm = system.return_quantity_spaces_available_motorcycles()
                qtdc = system.return_quantity_spaces_common_cars()
                qtdg = system.return_quantity_spaces_big_cars()
                janela4.hide()
                janela1 = self.init_window(qtdm, qtdc, qtdg)
            if window == janela1 and event == 'Ver relatório':
                janela1.hide()
                janela5 = self.report_window(system.return_number_big_cars_not_sparking(),
                                             system.return_number_common_cars_not_sparking(),
                                             system.return_number_mototcycles_not_sparking())
            if window == janela5 and event == 'Voltar':
                janela5.hide()
                qtdm = system.return_quantity_spaces_available_motorcycles()
                qtdc = system.return_quantity_spaces_common_cars()
                qtdg = system.return_quantity_spaces_big_cars()
                janela1 = self.init_window(qtdm, qtdc, qtdg)


# criando objeto do sistema de estacionamento
system = SystemParking()

##criando os espacos com os tipos das vagas
for index in range(1, 2):
    if index > 0 and index < 26:
        spaces_automobiles = SpacesAutomobile(index, True, "M")
    elif index > 25 and index < 51:
        spaces_automobiles = SpacesAutomobile(index, True, "G")
    else:
        spaces_automobiles = SpacesAutomobile(index, True, "C")
    # adicionando a vaga ao sistema de estacionamento
    system.insert_list_spaces_automobile(spaces_automobiles)

# iniciando
tela = TelaPython()
tela.iniciar(system)
