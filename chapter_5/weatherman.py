import report as wr

description = wr.get_description()
print("Today's weather:", description)
print(wr.get_description.__name__)
print(wr.get_description.__doc__)