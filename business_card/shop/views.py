from business_card.core.views import TemplateView


class ShopHomeView(TemplateView):

    template_name = 'shop/shop-home.html'

    def get(self, request):
        return self.render_to_response({})
