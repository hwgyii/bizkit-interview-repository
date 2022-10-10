from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    if len(args) == 0:
        return USERS
    
    result = []
    for query in args:
        for user in USERS:
            if user not in result:
                if query == "id" and user[query] == args[query]:
                    result.append(user)
                elif query == "name" and args[query].lower() in user[query].lower():
                    result.append(user)
                elif query == "age" and user[query] >= int(args[query]) - 1 and user[query] <= int(args[query]) + 1:
                    result.append(user)
                elif query == "occupation" and args[query].lower() in user[query].lower():
                    result.append(user)
    return result