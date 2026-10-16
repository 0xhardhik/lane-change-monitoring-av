"""
scenario_generator.py
Synthetic Multi-Lane Highway Scenario & Kinematic Simulation Engine.
Provides 3D-to-2D perspective projection, dynamic traffic generation,
and 3 interactive test scenarios (Cruise, Cut-in Hazard, Aborted Swerve).
"""

import math
import numpy as np

# Highway Geometry Constants
LANE_WIDTH = 3.7         # meters
NUM_LANES = 3            # Left (0), Center/Ego (1), Right (2)
ROAD_LENGTH = 120.0      # meters visible ahead

# Perspective Camera Parameters
CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
HORIZON_Y = 320          # Vanishing point horizon in screen pixels
FOCAL_LENGTH = 620.0     # Equivalent camera focal length in pixels
CAMERA_HEIGHT = 1.25     # Camera mounting height above road in meters


def world_to_screen(x_long, y_lat, z_height=0.0):
    """
    Projects 3D highway ground coordinates (in meters) to 2D screen pixels.
    x_long: Longitudinal distance forward from ego camera (meters, > 0.5)
    y_lat:  Lateral distance from ego lane center (meters, left is negative, right is positive)
    z_height: Vertical height above road surface (meters, road is 0.0)
    Returns: (u_pixel, v_pixel) or None if behind camera.
    """
    if x_long < 1.0:
        return None

    # Perspective division
    u = (CANVAS_WIDTH / 2.0) + (y_lat * FOCAL_LENGTH / x_long)
    v = HORIZON_Y + ((CAMERA_HEIGHT - z_height) * FOCAL_LENGTH / x_long)

    return int(u), int(v)


class VehicleAgent:
    """Represents a surrounding vehicle with kinematic state and bounding box."""

    def __init__(self, vehicle_id, initial_lane, initial_dx, initial_speed_kmh, color=(60, 60, 220), is_target=False):
        self.id = vehicle_id
        self.lane = initial_lane          # 0: Left, 1: Center, 2: Right
        self.dx = float(initial_dx)       # meters forward
        # Lateral position relative to center of ego lane (y=0)
        # Left lane center = -LANE_WIDTH (-3.7m), Right lane center = +LANE_WIDTH (+3.7m)
        self.dy = float((initial_lane - 1) * LANE_WIDTH)
        self.speed_kmh = float(initial_speed_kmh)
        self.vy = 0.0                     # lateral velocity (m/s)
        self.width = 1.9                  # meters
        self.length = 4.6                 # meters
        self.height = 1.5                 # meters
        self.color = color                # BGR
        self.is_target = is_target

    def update(self, dt, ego_speed_kmh):
        """Updates longitudinal position relative to ego vehicle and lateral position."""
        ego_vx_ms = ego_speed_kmh / 3.6
        target_vx_ms = self.speed_kmh / 3.6
        rel_vx_ms = target_vx_ms - ego_vx_ms

        self.dx += rel_vx_ms * dt
        self.dy += self.vy * dt

    def get_3d_box_corners(self):
        """Returns the 8 3D vertices (x, y, z) of the vehicle bounding box."""
        half_w = self.width / 2.0
        half_l = self.length / 2.0
        x = self.dx
        y = self.dy
        h = self.height

        # Front face (closest to camera = x - half_l)
        # Back face (further from camera = x + half_l)
        front_x = max(1.1, x - half_l)
        back_x = max(1.5, x + half_l)

        corners = [
            # Bottom 4 corners (z=0)
            (front_x, y - half_w, 0.0), # Bottom-Front-Left
            (front_x, y + half_w, 0.0), # Bottom-Front-Right
            (back_x,  y + half_w, 0.0), # Bottom-Back-Right
            (back_x,  y - half_w, 0.0), # Bottom-Back-Left
            # Top 4 corners (z=h)
            (front_x, y - half_w, h),   # Top-Front-Left
            (front_x, y + half_w, h),   # Top-Front-Right
            (back_x,  y + half_w, h),   # Top-Back-Right
            (back_x,  y - half_w, h)    # Top-Back-Left
        ]
        return corners


class HighwaySimulator:
    """Manages multi-lane highway scene and scenario orchestration."""

    def __init__(self):
        self.scenario_id = 1
        self.scenario_name = "Normal Highway Cruise"
        self.sim_time = 0.0
        self.ego_speed_kmh = 100.0
        self.target_speed_kmh = 95.0
        self.road_markings_offset = 0.0
        self.vehicles = []
        self.target_vehicle = None
        self.reset_scenario(1)

    def reset_scenario(self, scenario_id):
        """Initializes vehicle positions and parameters for the requested scenario."""
        self.scenario_id = scenario_id
        self.sim_time = 0.0
        self.road_markings_offset = 0.0

        if scenario_id == 1:
            # Scenario 1: Normal Highway Cruise
            self.scenario_name = "Normal Highway Cruise (Safe Following)"
            self.ego_speed_kmh = 100.0
            # Target car cruising in Left Lane at safe distance, maintaining lane
            self.target_vehicle = VehicleAgent(
                vehicle_id="Target-01", initial_lane=0, initial_dx=32.0,
                initial_speed_kmh=98.0, color=(80, 80, 220), is_target=True
            )
            # Ambient vehicle in Right Lane
            ambient1 = VehicleAgent(
                vehicle_id="Ambient-02", initial_lane=2, initial_dx=45.0,
                initial_speed_kmh=105.0, color=(180, 160, 60), is_target=False
            )
            # Lead vehicle in Center Lane far ahead
            ambient2 = VehicleAgent(
                vehicle_id="Ambient-03", initial_lane=1, initial_dx=65.0,
                initial_speed_kmh=102.0, color=(120, 120, 120), is_target=False
            )
            self.vehicles = [self.target_vehicle, ambient1, ambient2]

        elif scenario_id == 2:
            # Scenario 2: Aggressive Cut-in Hazard
            self.scenario_name = "Aggressive Cut-in Hazard (Proactive AEB)"
            self.ego_speed_kmh = 100.0
            # Target car in Left Lane, cuts in aggressively across lane delimiter
            self.target_vehicle = VehicleAgent(
                vehicle_id="Target-01", initial_lane=0, initial_dx=24.0,
                initial_speed_kmh=82.0, color=(40, 40, 240), is_target=True
            )
            # Ambient vehicle in Right Lane
            ambient1 = VehicleAgent(
                vehicle_id="Ambient-02", initial_lane=2, initial_dx=48.0,
                initial_speed_kmh=102.0, color=(180, 160, 60), is_target=False
            )
            self.vehicles = [self.target_vehicle, ambient1]

        elif scenario_id == 3:
            # Scenario 3: Aborted Swerve / False Alarm Suppression
            self.scenario_name = "Aborted Swerve / False Cut-in Recovery"
            self.ego_speed_kmh = 100.0
            # Target car in Left Lane, will drift toward center line then recover back
            self.target_vehicle = VehicleAgent(
                vehicle_id="Target-01", initial_lane=0, initial_dx=28.0,
                initial_speed_kmh=95.0, color=(60, 180, 240), is_target=True
            )
            ambient1 = VehicleAgent(
                vehicle_id="Ambient-02", initial_lane=2, initial_dx=44.0,
                initial_speed_kmh=98.0, color=(180, 160, 60), is_target=False
            )
            self.vehicles = [self.target_vehicle, ambient1]

    def update(self, dt, adas_state="CRUISE"):
        """Advances simulation by dt seconds and applies vehicle kinematics."""
        self.sim_time += dt

        # Modulate ego speed based on ADAS state and target headway
        target_ahead = self.target_vehicle and abs(self.target_vehicle.dy) < (LANE_WIDTH / 2.0)

        if adas_state == "EMERGENCY_AEB":
            # Sharp AEB deceleration (-6.5 m/s² ~ 23 km/h per second)
            min_speed = max(45.0, (self.target_vehicle.speed_kmh - 8.0) if self.target_vehicle else 50.0)
            self.ego_speed_kmh = max(min_speed, self.ego_speed_kmh - 22.0 * dt)
        elif adas_state == "CAUTION":
            # Smooth ACC throttle rollback (-1.5 m/s² ~ 5.4 km/h per second)
            min_speed = max(60.0, (self.target_vehicle.speed_kmh) if self.target_vehicle else 70.0)
            self.ego_speed_kmh = max(min_speed, self.ego_speed_kmh - 5.5 * dt)
        else:
            # Cruise mode: if target is safely in front, maintain safe following headway
            if target_ahead and self.target_vehicle.dx < 35.0:
                tgt_v = self.target_vehicle.speed_kmh
                if self.target_vehicle.dx < 14.0:
                    self.ego_speed_kmh = max(40.0, self.ego_speed_kmh - 6.0 * dt)
                elif self.target_vehicle.dx > 18.0:
                    self.ego_speed_kmh = min(tgt_v + 4.0, self.ego_speed_kmh + 3.0 * dt)
                else:
                    self.ego_speed_kmh = tgt_v
            else:
                # Normal road cruising: accelerate back to 100 km/h
                if self.ego_speed_kmh < 100.0:
                    self.ego_speed_kmh = min(100.0, self.ego_speed_kmh + 4.5 * dt)

        # Advance road dashed lines
        ego_speed_ms = self.ego_speed_kmh / 3.6
        self.road_markings_offset = (self.road_markings_offset + ego_speed_ms * dt) % 12.0

        # Orchestrate scenario kinematics for target vehicle
        if self.target_vehicle:
            if self.scenario_id == 1:
                # Normal cruise: subtle natural lane wobble
                self.target_vehicle.vy = 0.04 * math.sin(self.sim_time * 1.5)
                # Keep target dx within comfortable buffer (25m - 40m)
                if self.target_vehicle.dx < 26.0:
                    self.target_vehicle.speed_kmh = 101.5
                elif self.target_vehicle.dx > 38.0:
                    self.target_vehicle.speed_kmh = 96.5

            elif self.scenario_id == 2:
                # Aggressive Cut-in:
                # 0 to 1.0s: cruises in left lane
                # 1.0 to 3.4s: aggressive lateral cut into center lane (vy = +1.15 m/s)
                # >3.4s: settled in center lane (dy = 0.0)
                if self.sim_time < 1.0:
                    self.target_vehicle.vy = 0.0
                elif 1.0 <= self.sim_time < 3.4:
                    if self.target_vehicle.dy < 0.0:
                        self.target_vehicle.vy = 1.15  # moving towards right into center
                    else:
                        self.target_vehicle.vy = 0.0
                        self.target_vehicle.dy = 0.0
                else:
                    self.target_vehicle.vy = 0.0
                    self.target_vehicle.dy = 0.0  # safely settled in ego lane

                # Target decelerates during cut-in to heighten collision urgency
                if 1.1 <= self.sim_time <= 2.6:
                    self.target_vehicle.speed_kmh = max(65.0, self.target_vehicle.speed_kmh - 14.0 * dt)

                # Seamless loop after demonstration (after 8 seconds)
                if self.sim_time > 8.0:
                    self.reset_scenario(2)

            elif self.scenario_id == 3:
                # Aborted Swerve:
                # 0 to 1.0s: cruises in left lane
                # 1.0 to 2.2s: drifts towards lane line (vy = +0.80 m/s)
                # 2.2 to 3.5s: driver recovers! vy reverses to -0.85 m/s moving back left
                # >3.5s: safely re-centered in left lane (dy = -LANE_WIDTH)
                if self.sim_time < 1.0:
                    self.target_vehicle.vy = 0.0
                elif 1.0 <= self.sim_time < 2.2:
                    self.target_vehicle.vy = 0.80  # drifting right towards ego line
                elif 2.2 <= self.sim_time < 3.5:
                    self.target_vehicle.vy = -0.85 # recovering back to left!
                else:
                    self.target_vehicle.vy = 0.0
                    self.target_vehicle.dy = -LANE_WIDTH  # safe in left lane

                # Seamless loop after demonstration
                if self.sim_time > 8.0:
                    self.reset_scenario(3)

        # Update all vehicles
        for v in self.vehicles:
            v.update(dt, self.ego_speed_kmh)

        # Respawn only ambient background vehicles if they pass too far behind or ahead
        # Target vehicle is never teleported!
        for v in self.vehicles:
            if not v.is_target:
                if v.dx < 2.0:
                    v.dx = 85.0
                elif v.dx > 105.0:
                    v.dx = 30.0
