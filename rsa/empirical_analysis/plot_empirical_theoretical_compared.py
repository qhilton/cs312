import json
import matplotlib.pyplot as plt


def main():

    # COMMENT AND UNCOMMENT appropriate lines as necessary

    # filename = "_primes_runtimes.json"
    # filename = '_keypairs_runtimes.json'
    # filename = '_encryption_runtimes.json'
    filename = '_decryption_runtimes.json'

    with open(filename, "r") as f:
        runtimes = json.load(f)

    # FILL THIS IN with your theoretical time complexity
    def theoretical_big_o(n):
        return n**2

    # FILL THIS IN from result using compute_coefficient
    # coeff = 4.7016372716387105e-09 # primes_runtimes
    # coeff = 9.093222743302338e-09 # keypairs_runtimes
    # coeff = 1.7656776511998374e-08 # encryption_runtimes 0.00011194044724106789
    coeff = 7.486546892778279e-05 # decryption_runtimes 8.133945191213243e-07

    nn = [n for n, _ in runtimes]
    times = [t for _, t in runtimes]

    # Plot empirical values
    fig = plt.figure()
    plt.scatter(nn, times, marker="o")

    predicted_runtime = [coeff * theoretical_big_o(n) for n, t in runtimes]

    # Plot theoretical fit
    plt.plot(nn, predicted_runtime, c="k", ls=":", lw=2, alpha=0.5)

    # Update title, legend, and axis labels as needed
    plt.legend(["Observed", "Theoretical O(n)"])
    plt.xlabel("n")
    plt.ylabel("Runtime")
    plt.title("Time for Decryption")

    fig.show()
    fig.savefig("empirical.svg")


if __name__ == "__main__":
    main()
