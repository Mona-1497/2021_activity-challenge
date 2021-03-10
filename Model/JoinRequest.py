class JoinRequest:
    def __init__(self, teamID, managerMail, userMail, confirm, dateRequest):
        self.teamID = teamID
        self.managerMail = managerMail
        self.userMail = userMail
        self.confirm = confirm
        self.dateRequest = dateRequest