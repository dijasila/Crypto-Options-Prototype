python
Copy code
# main.py

from experiments import experiment_1, experiment_2

def main():
    print("Running Experiment 1...")
    experiment_1.run_experiment()
    print("Running Experiment 2...")
    experiment_2.run_experiment()

if __name__ == "__main__":
    main()