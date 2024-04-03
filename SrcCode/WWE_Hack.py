from uniref import WinUniRef

def GetProcess():
    return WinUniRef("World Warfare & Economics.exe")

class Hack:
    def AllowMAXBUDGET():
        uniref_unity = GetProcess()
        yearlybudgetclass = uniref_unity.find_class_in_image("WWE", "YearlyBudget")
        setmaxbudget = yearlybudgetclass.find_field("AllowMaxBudget")
        for addr in yearlybudgetclass.guess_instance_address():
            setmaxbudget.instance = bool(addr)
            if bool(addr) is False:
                setmaxbudget.instance = addr
                setmaxbudget.value = True
                print(setmaxbudget.value)