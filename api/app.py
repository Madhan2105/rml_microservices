from flask import Flask, request, jsonify
from models import Tasks
from database import DatabaseConnection

app = Flask(__name__)

DatabaseConnection(
    app
)

@app.route("/health", methods=["GET"])
def get_health():
    """Return healh of the microservice."""
    return jsonify({"health": "okay"})


@app.route("/data", methods=["GET"])
def get_data():
    """Retreive all the Task Data."""
    page = request.args.get('page', default=1, type=int)
    page_size = request.args.get('page_size', default=10, type=int)
    search = request.args.get('search', default=None, type=str)

    query = Tasks.query

    if search:
        query = query.filter(Tasks.description.ilike(f'%{search}%'))

    paginated_query = query.paginate(
        page=page, per_page=page_size, error_out=False
    )
    tasks = paginated_query.items

    response = {
        "tasks": [
            {
                "id": task.id,
                "description": task.description,
            }
            for task in tasks
        ],
        "total": paginated_query.total,
        "pages": paginated_query.pages,
        "current_page": paginated_query.page,
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
