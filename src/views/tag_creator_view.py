from src.views.http_types.http_resquest import HttpRequest
from src.views.http_types.http_reponse import HttpResponse
from src.controllers.tag_creator_controller import  TagCreatorController

class TagCreatorView:

  def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
    tag_creator_controller = TagCreatorController()

    body = http_request.body
    product_code = body["product_code"]

    formatted_reponse = tag_creator_controller.create(product_code)
  
    return HttpResponse(status_code=200, body=formatted_reponse)
