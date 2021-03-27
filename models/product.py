from models.base import Base

class Product(Base):
    def __init__(self, *args, **kwargs):
        self.price = 0
        self.name = ''
        self.description = ''
        self.in_stock = 0
        self.image_url = 'https://media.istockphoto.com/photos/open-cardboard-box-picture-id173831957?k=6&m=173831957&s=612x612&w=0&h=Lia7nWeOi0dOBJElI8tRmfoMqEQ_sNBjKbydZoJ3V_w='
        super().__init__(*args, **kwargs)