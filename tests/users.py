class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f"<User {self.name}>"


def get_user_score(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorrect values provided to our calculation function.")
        raise  # raise an exception and bubbling it up the call stack
    else:
        print("User score is", user.score)


def email_engaged_user(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorrect values provided to our calculation function.")
    else:
        if user.score > 500:
            send_engagement_notification(user)


def perform_calculation(metrics):
    return metrics["clicks"] * 5 + metrics["hits"] * 2


def send_engagement_notification(user):
    print(f"Notification sent to {user}.")


my_user = User("Rolf", {"clicks": 61, "hits": 100})
email_engaged_user(my_user)
error_user = User("Error User", {"click": 61, "hit": 100})
email_engaged_user(error_user)
get_user_score(error_user)
