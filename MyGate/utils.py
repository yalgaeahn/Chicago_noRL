import numpy as np
import qutip
import matplolib.pyplot as plt

def get_Bloch_vec(state):
    """
    :param state: single qubit state, ndarray of shape (2,)
    :return:
    """
    alpha = state[0]
    beta = state[1]
    rho01=alpha*np.conj(beta)
    x = 2*rho01.real
    y = 2*rho01.imag
    z = np.absolute(alpha)**2-np.absolute(beta)**2

    return np.array([x,y,z])


