def decoreer(tekst="", limiet=1):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()
    
    if limiet > 1:
        decoreer("Aanbieding", limiet - 1)  # Verminder de limiet voor elke recursieve oproep