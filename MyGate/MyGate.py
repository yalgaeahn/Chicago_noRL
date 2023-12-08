import numpy as np
import torch


def make_U(H, time_step):
    hbar = 1.
    I = np.identity(4, dtype=complex)

    def U(t):
        total = I  # U(t=0)
        check = [I]
        times = np.arange(start=0, stop=t, step=time_step)
        for time in times:
            derivative = (-1j / hbar) * np.matmul(H(time), total) * time_step
            total = total + derivative
            check.append(total)
            return total, np.array(check)

        return U


def make_H_int(g, delta_omega):
    def H_int(t):
        matrix = np.zeros((4, 4), dtype=complex)
        matrix[2][1] = np.exp(1j * delta_omega * t)
        matrix[1][2] = np.exp(-1j * delta_omega * t)
        return g(t) * matrix

    return H_int
