html = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Gallery</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="bootstrap-gallery/styles.css">
</head>
<!-- Gallery -->
<!-- 
Gallery is linked to lightbox using data attributes.

To open lightbox, this is added to the gallery element: {data-toggle="modal" data-target="#exampleModal"}.

To open carousel on correct image, this is added to each image element: {data-target="#carouselExample" data-slide-to="0"}.
Replace '0' with corresponding slide number.
-->
<body>
<div class="row" id="gallery" data-toggle="modal" data-target="#exampleModal">

{% for image in images %}
  <div class="col-12 col-sm-6 col-lg-3">
    <img class="w-100" src="thumbs/{{image}}" alt="First slide" data-target="#carouselExample" data-slide-to="{{images.index(image)}}">
  </div>
{% endfor %}
</div>

<!-- Modal -->
<!-- 
This part is straight out of Bootstrap docs. Just a carousel inside a modal.
-->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <div id="carouselExample" class="carousel slide" data-ride="carousel">
          <!-- <ol class="carousel-indicators">
            <li data-target="#carouselExample" data-slide-to="0" class="active"></li>
            {% for image in images %}
              <li data-target="#carouselExample" data-slide-to="{{images.index(image)}}"></li>
            {% endfor %}
          </ol> -->
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img class="d-block w-100" src="large_imgs/{{images[0]}}" alt="First slide">
            </div>

            {% for image in images[1:] %}
            <div class="carousel-item">
              <img class="d-block w-100" src="large_imgs/{{image}}" alt="Second slide">
            </div>
            {% endfor %}

          </div>
          <a class="carousel-control-prev" href="#carouselExample" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#carouselExample" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</body>
</html>
"""