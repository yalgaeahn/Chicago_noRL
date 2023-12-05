import numpy as np


class single_qubit:
    def make_U(hbar=1.,H, time_step):
        """
        PARAMETER
            hbar : float
            Hamiltonian : function of t
            time_step : float
        RETURNS
            U : function of t
        """
        hbar = 1.
        I = np.identity(2, dtype="complex128")

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