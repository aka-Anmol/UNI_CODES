#get the shipment type
shipment = input("Is it a domestic shipment or international? ")
shipmenttype = input("Is it a standard or express? ")

if shipment == "domestic" and shipmenttype == "standard":
    print("The cost of the shipment domestic standard  is : £5.99")
else:
    print("The cost of the shipment domestic express is : £7.99")

if shipment == "internattional" and shipmenttye == "standard":
    print("The cost of the shipment international standard is : £10.99")
else:
    print("The cost of the shipment international express is : £14.99")
    
