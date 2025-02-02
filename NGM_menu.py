from pybricks.hubs import PrimeHub
from pybricks.tools import hub_menu
from pybricks.parameters import Axis

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)

if hub.imu.ready():
    selected = hub_menu("A", "B", "C", "D", "E", "F", "G")
    if selected == "A" :
        import NGM_1_new
    elif selected == "B" :
        import NGM_2
    elif selected == "C" :
        import NGM_3
    elif selected == "D" :
        import NGM_4
    elif selected == "E" :
        import NGM_5
    elif selected == "F" :
        import NGM_6
    elif selected == "G" :
        import NGM_7