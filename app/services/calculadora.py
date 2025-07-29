#TODO: Agregar "ganancia real descontando inflación proyectada"_
from app.models.calculo import CalculoRequest, DetallePeriodo, PeriodoCapitalizacion,FrecuenciaAporte


import pandas as pd

class InteresCompuestoBase:
    def __init__(self, capital_inicial, tasa_interes_anual, anios, periodo_cap: PeriodoCapitalizacion):
        self.capital_inicial = capital_inicial
        self.tasa_interes_anual = tasa_interes_anual / 100
        self.anios = anios
        self.periodo_cap = periodo_cap
        self.tipo_capitalizacion = {
            "anual": 1,
            "semestral": 2,
            "trimestral": 4,
            "mensual": 12
        }[self.periodo_cap.value]
        self.tasa_periodica = self.tasa_interes_anual / self.tipo_capitalizacion
        self.total_periodos = int(self.tipo_capitalizacion * self.anios)

    def calcular(self):
        raise NotImplementedError("Debe implementarse en la subclase")
    
class InteresCompuestoSimple(InteresCompuestoBase):
    def calcular(self):
        monto_final = self.capital_inicial * (1 + self.tasa_periodica) ** self.total_periodos
        detalle_df = pd.DataFrame(columns=["capital_final", "ganancia_total"])
        detalle_df.loc[len(detalle_df)] = [round(monto_final, 2),round(monto_final-self.capital_inicial, 2)]
        detalle = detalle_df.to_dict(orient="records")
        return {
            "capital_final": round(monto_final, 2),
            "ganancia_total": round(monto_final - self.capital_inicial, 2),
            "detalle":detalle
        }
    

class InteresCompuestoConAportes(InteresCompuestoBase):
    def __init__(self, capital_inicial, tasa_interes_anual, anios, periodo_cap, aportes_periodicos, cada_cuanto_aporta:FrecuenciaAporte):
        super().__init__(capital_inicial, tasa_interes_anual, anios, periodo_cap)
        self.aportes_periodicos = aportes_periodicos
        self.aportes_por_anio = cada_cuanto_aporta.value
        if self.aportes_periodicos:
            self.frecuencia_aporte = {
                "anual": 1,
                "semestral": 2,
                "cuatrimestral": 3,
                "trimestral": 4,
                "bimestral": 6,
                "mensual": 12
            }[cada_cuanto_aporta.value]

    def calcular(self):
        #Generación del dataframe y primer detalle
        df_detalle = pd.DataFrame(columns=["anio", "periodo", "capital_actual", "interes_generado", "interes_acumulado", "monto_agregado"])
        df_detalle.loc[len(df_detalle)] = [0, "Inicial", self.capital_inicial, 0, 0, 0]
        
        #Calculadora de meses de aporte y capitalización
        def calc_meses(capitalizacion_o_aportes:int):
            meses_que_aplica = 12/capitalizacion_o_aportes
            return {mes+1 for mes in range(12) if (mes+1) % meses_que_aplica == 0}
        
        meses_que_paga = calc_meses(self.tipo_capitalizacion)
        meses_que_agrega = calc_meses(self.frecuencia_aporte)

        #Cálculo
        periodo = 0
        capital_acumulado = self.capital_inicial
        capital_anual = 0
        ganancia_total = 0
        for anio in range(self.anios):
            for mes in range(12):
                if (mes+1) in meses_que_paga:
                    periodo += 1
                    interes_devengado = round(capital_acumulado * self.tasa_periodica,2)
                    capital_acumulado += interes_devengado
                    ganancia_total += interes_devengado
                    df_detalle.loc[len(df_detalle)] = [int(anio+1),periodo, capital_acumulado, interes_devengado,ganancia_total, capital_anual]

                if (mes+1) in meses_que_agrega:
                    capital_acumulado += self.aportes_periodicos
                    capital_anual += self.aportes_periodicos
        detalle = [DetallePeriodo(**fila) for fila in df_detalle.to_dict(orient="records")]
        resultado = {
            "capital_final": round(capital_acumulado,2),
            "ganancia_total" : round(ganancia_total,2),
            "detalle": detalle}
        return resultado

def calcular_interes_compuesto(data: CalculoRequest):
    if data.aportes_periodicos:
        modelo = InteresCompuestoConAportes(
    capital_inicial=data.capital_inicial,
    tasa_interes_anual=data.tasa_interes_anual,
    anios=data.anios,
    periodo_cap=data.tipo_capitalizacion,  
    aportes_periodicos=data.aportes_periodicos,
    cada_cuanto_aporta=data.cada_cuanto_aporta
)

    else:
        modelo = InteresCompuestoSimple(capital_inicial=data.capital_inicial,
    tasa_interes_anual=data.tasa_interes_anual,
    anios=data.anios,
    periodo_cap=data.tipo_capitalizacion)
    return modelo.calcular()




