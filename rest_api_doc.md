
_cycle/MeasuredCycleTime	... ms
_meta/Version				... string

**meter0/**   ...  hy-switch

**ess0/**   ...  battery

**charger0/**   ...  PV-Anlage

**_sum/**		...  General - All

| *Bezeichnung*                     | *Channel-ID*                                                 | Einheit        |
| --------------------------------- | ------------------------------------------------------------ | -------------- |
| **Batterie**                      | **ess0**                                                     |                |
| Status                            | State                                                        | 0 (Ok)         |
| Ladezustand                       | Soc                                                          | %              |
| On-Off-Grid-Status                | GridMode                                                     |                |
| Be-/Entladeleistung               | ActivePower                                                  | W              |
| Blindleistung                     | ReactivePower                                                | W              |
| Belade-Energie                    | ActiveChargeEnergy                                           | Wh             |
| Entlade-Energie                   | ActiveDischargeEnergy                                        | Wh             |
| Erlaubte Beladeleistung           | AllowedChargePower                                           | W              |
| Erlaubte Entladeleistung          | AllowedDischargePower                                        | W              |
|                                   | SetActivePowerEquals, SetActivePowerLessOrEquals, SetReactivePowerEquals, SetActivePowerGreaterOrEquals |                |
|                                   |                                                              |                |
|                                   |                                                              |                |
|                                   |                                                              |                |
| **PV-Anlage**                     | **charger0**                                                 |                |
| Status                            | State                                                        | 0 (Ok)         |
| Leistung                          | ActualPower                                                  | W              |
| Energie                           | ActualEnergy                                                 | Wh             |
| Maximale Leistung                 | MaxActualPower                                               | W              |
|                                   |                                                              |                |
|                                   |                                                              |                |
|                                   |                                                              |                |
|                                   |                                                              |                |
| **Hy-switch (Netzzähler)**        | **meter0**                                                   |                |
| Status                            | State                                                        | 0 (Ok)         |
| Frequenz                          | Frequency                                                    | mHz            |
| Netzbezugs-/Netzeinspeiseleistung | ActivePower, ActivePowerL1, ActivePowerL2, ActivePowerL3     | W              |
| Blindleistung                     | ReactivePower, ReactivePowerL1, ReactivePowerL2, ReactivePowerL3 | W              |
| Netzbezugsenergie                 | ActiveProductionEnergy                                       | Wh             |
| Netzeinspeiseenergie              | ActiveConsumptionEnergy                                      | Wh             |
| Spannung                          | Voltage, VoltageL1, VoltageL2, VoltageL3                     | mV             |
| Strom                             | Current, CurrentL1, CurrentL2, CurrentL3                     | mA             |
| Maximale, Minimale Leistung       | MaxActivePower, MinActivePower                               | W              |
|                                   |                                                              |                |
|                                   |                                                              |                |
|                                   |                                                              |                |
| **Allgemein**                     | **_sum**                                                     |                |
|                                   | ConsumptionActiveEnergy                                      | Wh             |
|                                   | ConsumptionActivePower, ConsumptionActivePowerL1, ConsumptionActivePowerL2,  ConsumptionActivePowerL3 | W              |
|                                   | ConsumptionMaxActivePower                                    | W              |
|                                   | EssActiveChargeEnergy, EssActiveDischargeEnergy              | Wh             |
|                                   | EssActivePower, EssActivePowerL1, EssActivePowerL2, EssActivePowerL3 | W              |
|                                   | EssCapacity                                                  | Wh             |
|                                   | EssMaxApparentPower                                          | VA             |
|                                   | EssSoc                                                       | %              |
|                                   | GridActivePower, GridActivePowerL1, GridActivePowerL2, GridActivePowerL3 | W              |
|                                   | GridBuyActiveEnergy                                          | Wh             |
|                                   | GridMaxActivePower, GridMinActivePower                       | W              |
|                                   | GridMode                                                     | -1 (Undefined) |
|                                   | GridSellActiveEnergy                                         | Wh             |
|                                   | ProductionAcActiveEnergy                                     | Wh             |
|                                   | State                                                        | 0 (Ok)         |
|                                   | ProductionAcActivePower, ProductionAcActivePowerL1,  ProductionAcActivePowerL2,  ProductionAcActivePowerL3 | W              |
|                                   | ProductionActiveEnergy                                       | Wh             |
|                                   | ProductionActivePower                                        | W              |
|                                   | ProductionDcActiveEnergy                                     | Wh             |
|                                   | ProductionDcActualPower                                      | W              |
|                                   | ProductionMaxAcActivePower                                   | W              |
|                                   | ProductionMaxActivePower                                     | W              |
|                                   | ProductionMaxDcActivePower                                   | W              |
|                                   |                                                              |                |
|                                   |                                                              |                |
|                                   |                                                              |                |
|                                   |                                                              |                |

