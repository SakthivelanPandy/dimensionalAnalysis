import numpy as np

def read_dimensions(string):
    #converts a string into a list of dimensions, in the order MLT. e.g. "1 0 1" represent M^1 L^0 T^1 and gets converted to [1,0,1]
    return [int(x) for x in string.split(" ")]

def multiply_dimensions(dimension1, dimension2):
    #multiplies two dimensions together by adding the indices of each dimension together
    return [dimension1[0] + dimension2[0], dimension1[1] + dimension2[1], dimension1[2] + dimension2[2]]

def dimension_exponent(dimension,exp):
    #multiplies a dimension by an exponent, by multiplying each index by the exponent
    return [dimension[0] * exp, dimension[1] * exp, dimension[2] * exp]

def print_dimensions(dimension):
    #formats the output of a dimension
    print(f"M^{dimension[0]} L^{dimension[1]} T^{dimension[2]}")

def calc_dimension(*dimensions_and_exp):
    #calculates exponents of each dimension, and multiplies them together
    dimensions = []
    for i in dimensions_and_exp:
        new_dimension = dimension_exponent(i[0],i[1])
        dimensions.append(new_dimension)
    d1 = dimensions[0]
    for i in range(1,len(dimensions)):
        d1 = multiply_dimensions(d1,dimensions[i])
    return d1

def calc_exponents(target,*dimensions):
    m = []
    l = []
    t = []
    for i in dimensions:
        m.append(i[0])
        l.append(i[1])
        t.append(i[2])
    e = [m,l,t]
    res = np.linalg.inv(e).dot(target)
    return res


def main():
    d1 = "1 0 0"  #representing M^1 L^0 T^0, Mass
    d2 = "1 0 -2" #representing M^1 L^0 T^-2, Spring Constant
    d3 = "0 1 0" #representing M^0 L^1 T^0, Length

    #convert the strings into lists of dimensions
    d1 = read_dimensions(d1)
    d2 = read_dimensions(d2)
    d3 = read_dimensions(d3)
    
    #calculate new dimensions
    new_d = calc_dimension((d1,-0.5),(d2,0.5),(d3,1))
    print_dimensions(new_d)

    #find exponents
    target = [0,1,-1]
    res = calc_exponents(target,d1,d2,d3)
    print(res)

if __name__ == "__main__":
    main()
