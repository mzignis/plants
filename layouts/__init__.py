from layouts.index import index_layout
from layouts.errors import error_404
from layouts.plants import plant1_page

layouts_ = {
    'index': index_layout,
    'plant1': plant1_page,
    '404': error_404,
}