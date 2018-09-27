function getId(id, value) {
    idm = '#modal' + value
    console.log(idm)
    $(idm).removeClass('d-none');
    $('.overlay').removeClass('d-none');
}

$('.overlay').click(function (e) {
    e.preventDefault();
    $('.one-image').addClass('d-none');
    $(this).addClass('d-none');
});

$('.modal-img').click(function (e) {
    e.preventDefault();
    $(this).toggleClass('modal-img-lg');
    $(this).toggleClass('modal-img-sm');
    // $(selector).toggleClass(className);
});