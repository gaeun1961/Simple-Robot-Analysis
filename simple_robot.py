import pybullet as p
import pybullet_data
import os
import time
import pandas as pd

base_path = pybullet_data.getDataPath().replace("\\", "/")
plane_path = f"{base_path}/plane.urdf"
robot_path = f"{base_path}/kuka_iiwa/model.urdf"

p.connect(p.GUI)
p.setGravity(0, 0, -9.81)

try:
    p.loadURDF(plane_path)
    robot_id = p.loadURDF(robot_path, [0, 0, 0], useFixedBase=True)
    print("[+] 로봇 로드 완료 / 데이터 수집을 시작")

    log_data = []

    for i in range(157):
        target_pos = i * 0.01
        
        p.setJointMotorControl2(bodyIndex=robot_id, 
                                 jointIndex=1, 
                                 controlMode=p.POSITION_CONTROL, 
                                 targetPosition=target_pos)
        
        p.stepSimulation()
        
        joint_state = p.getJointState(robot_id, 1)
        actual_pos = joint_state[0]
        actual_vel = joint_state[1]
        
        log_data.append([time.time(), target_pos, actual_pos, actual_vel])
        
        time.sleep(1./240.)

    print("수집 완료 / CSV 파일 생성")
    
    df = pd.DataFrame(log_data, columns=['timestamp', 'target_pos', 'actual_pos', 'velocity'])
    df.to_csv("robot_trajectory_log.csv", index=False)
    print(f"'robot_trajectory_log.csv' 파일이 저장 완료")

    time.sleep(10)

except Exception as e:
    print(f"에러 발생: {e}")

finally:
    p.disconnect()