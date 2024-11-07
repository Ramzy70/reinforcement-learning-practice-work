import matplotlib.pyplot as plt

# plot function
def plotting(num_steps,average_rewards,optimal_actions, plot_label):
    plt.figure(figsize=(16, 8))

    # Average Reward vs. Number of Steps
    plt.subplot(1, 2, 1)
    for index, epsilon in enumerate(plot_label):
        plt.plot(range(num_steps), average_rewards[index], label=plot_label[index])
    plt.xlabel('Number of Steps')
    plt.ylabel('Average Reward')
    plt.legend()

    # Optimal Actions vs. Number of Steps
    plt.subplot(1, 2, 2)
    for index, epsilon in enumerate(plot_label):
        plt.plot(range(num_steps), optimal_actions[index] * 100, label=plot_label[index])
    plt.xlabel('Number of Steps')
    plt.ylabel('% Optimal Action')
    plt.ylim(0, 100)
    plt.legend()

    plt.tight_layout()
    plt.show()

