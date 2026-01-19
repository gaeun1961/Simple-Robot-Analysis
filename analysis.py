import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('robot_trajectory_log.csv')

df['error'] = df['target_pos'] - df['actual_pos']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# graph 1
ax1.plot(df.index, df['target_pos'], label='Target (명령)', color='blue', linewidth=2)
ax1.plot(df.index, df['actual_pos'], label='Actual (실제)', color='orange', linestyle='--', linewidth=2)
ax1.set_ylabel('Position (Radians)')
ax1.set_title('Robot Joint Trajectory: Target vs Actual')
ax1.legend()
ax1.grid(True)

# graph 2
ax2.plot(df.index, df['error'], label='Tracking Error (오차)', color='red')
ax2.set_xlabel('Simulation Step')
ax2.set_ylabel('Error (Radians)')
ax2.set_title('Joint Tracking Error Analysis')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

print("\n----- 오차 분석 통계 -----")
print(f"평균 오차: {df['error'].mean():.4f} rad")
print(f"최대 오차: {df['error'].max():.4f} rad")