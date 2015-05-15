import numpy as np

A = [[-5, 0.03, 2], [0, -800, 0], [-1, -0.005, -2]]
a = [2, 4, 6]
bc = [1/6, 5/6]
bb = [1/2, 1/2]
ba = [[1/6, 0], [4/6, 1/6]]
# h from 0 to sqrt(3)-1
h = .01

def k1( t, u, k ):
    return k - f( t + bc[0] * h, u + np.inner( k, ba[0][0] * h ) )

def def_k1(t, u, k):
    return np.matrix( [[1]] * 3) - np.inner( def_f(t + bc[0] * h, u + np.inner( k, ba[0][0] * h )), ba[0][0] * h )

def f( t, g ):
    return np.matrix( A ) * g

def def_f(t, g ):
    return f(t, f(t, g))
    pass

def u( x ):
    # for i in  A
    pass

def R( z ):
    bbt = np.matrix( bb )
    bam = np.matrix( ba )
    e = np.matrix( "1; 1" )
    inv = np.linalg.inv( np.eye( 2 ) - np.inner( bam, z ) )
    return (np.matrix( "1" ) +  np.dot( np.inner( bbt, z ), inv ) * e).item(0)

def R_analit( z ):
    return (1 + z - 5 * z ** 2 / 36) / (1 - z / 6) ** 2

if __name__ == '__main__':

    for i in range(5):
        print(i, R(i), R_analit(i))

    ls, vect = np.linalg.eig( np.matrix(A) )
    lmin = np.amin(np.abs(ls))
    lmax = np.amax(np.abs(ls))
    s = lmax / lmin
    print(lmin, lmax, s)

    '''start = 0
    end =  1
    N = (end - start) / h
    k = [[[np.matrix([[0]]*3)]], [[np.matrix([[0]]*3)]]]
    u = [np.matrix([[2], [4], [6]]), ]
    t = []
    eps = .001



    iter = 0
    while True:
        t.append(start + h * iter)
        k[0].append([np.matrix([[0]]*3)])
        k[1].append([np.matrix([[0]]*3)])
        lit = 0
        while True:
            k[0][iter].append( f( t[iter] + bc[0] * h, u[iter] + h * ba[0][0] * k[0][iter][lit] + h * ba[0][1] * k[1][iter][lit] ) )
            k[1][iter].append( f( t[iter] + bc[1] * h, u[iter] + h * ba[1][0] * k[0][iter][lit] + h * ba[1][1] * k[1][iter][lit] ) )

            if ( (np.any( np.less( np.absolute( np.subtract(np.absolute(k[0][iter][lit+1]), np.absolute(k[0][iter][lit])) ), np.matrix([[eps]]*3) ) ) and
                     np.any( np.less( np.absolute( np.subtract(np.absolute(k[1][iter][lit+1]), np.absolute(k[1][iter][lit])) ), np.matrix([[eps]]*3) ) )) or lit >= 10 ):
                # print( "break for k", lit )
                ## print( np.less( np.absolute( np.subtract(k[0][iter][lit+1], k[0][iter][lit]) ), np.matrix([[eps]]*3)) )
                # print( np.absolute(k[0][iter][lit+1]), np.absolute(k[0][iter][lit]), np.matrix([[eps]]*3) )
                break
            lit += 1
        u.append( u[iter] + np.matrix( h* (bb[0]*k[0][iter][-1] + bb[1]*k[1][iter][-1]) ) )
        if iter == 2 or t[iter] >= end:
            # print( "break for u", iter )
            break
        iter += 1
        pass

    # print(k[0][iter])
    #print(k[1][-2])
    #print(u[-1], t[-1])'''

'''
http://m2matlabdb.ma.tum.de/exercise/rk60_eng.pdf?ME_ID=121&target=pdf
http://www.iit.bas.bg/PECR/62/24-42.pdf
http://rosettacode.org/wiki/Runge-Kutta_method#Python
'''
