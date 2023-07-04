import roboticstoolbox as rtb
import mpl_toolkits.mplot3d.art3d as art3d


def plot_baseplate(env=None):
    """
        Plot the base plate as a 3D rectangle using a given plotting environment.

        Parameters:
            env (roboticstoolbox.backends.PyPlot.PyPlot, optional):
                Plotting environment to use. If not provided, a new instance of `PyPlot` backend will be created
                and launched. Default is None.

        Returns:
            roboticstoolbox.backends.PyPlot.PyPlot:
                The plotting environment used to render the base plate.

        Raises:
            TypeError:
                If `env` is provided but it is not an instance of `roboticstoolbox.backends.PyPlot.PyPlot`.

        """

    # Handle backend input
    if env is None:
        env = rtb.backends.PyPlot.PyPlot()
        env.launch()
    elif type(env) is not rtb.backends.PyPlot.PyPlot:
        raise TypeError('Plotting environment must be a PyPlot backend. Swift is not supported.')

    # Define the base plate dimensions and coordinates
    x = [-0.15, 0.6, 0.6, -0.15, -0.15]
    y = [-0.55/2, -0.55/2, 0.55/2, 0.55/2, -0.55/2]
    z = [0, 0, 0, 0, 0]

    vertices = [list(zip(x, y, z))]

    rectangle = art3d.Poly3DCollection(vertices, edgecolor='grey', facecolor='grey', alpha=0.5)

    env.ax.add_collection3d(rectangle)
    env.ax.auto_scale_xyz([-0.15, 0.60], [-0.55/2, 0.55/2], [0, 0.7])

    return env