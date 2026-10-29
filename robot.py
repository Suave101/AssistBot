import wpilib
import wpilib.drive
import xrp

class XRPBot(wpilib.TimedRobot):
    def robotInit(self):
        self.left_motor = xrp.XRPMotor(0)
        self.right_motor = xrp.XRPMotor(1)
        self.right_motor.setInverted(True)
        self.drivetrain = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

        # Switch from XboxController to generic Joystick for keyboard support
        self.controller = wpilib.Joystick(0)

        self.gyro = xrp.XRPGyro()
        self.rangefinder = xrp.XRPRangefinder()

    def robotPeriodic(self):
        wpilib.SmartDashboard.putNumber("Gyro Pitch", self.gyro.getAngle())
        wpilib.SmartDashboard.putNumber("Range (cm)", self.rangefinder.getDistance() * 100)

    def teleopPeriodic(self):
        # Use getY() and getX() for keyboard input
        forward = -self.controller.getY()
        turn = self.controller.getX()
        self.drivetrain.arcadeDrive(forward, turn)

if __name__ == "__main__":
    wpilib.startRobot(XRPBot)
