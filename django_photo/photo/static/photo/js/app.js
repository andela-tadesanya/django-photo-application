$(document).foundation();
$(document).ready( function () {
    var deleteFtr = {
        $delete: $('.delete-btn'),
        onDelete: function (event) {
            event.preventDefault();
            var $form = $(this).parent();
            var id = $(this).data('id');
            var postData = {};

            $form.find('input').each(function (i, el) {
                $el = $(el);
                postData[$el.attr('name')] = $el.val();
            });
            var url = $form.attr('action');
            var $statusBox = $('.sidebar-status');

            $.post(url, postData).done(function (resp) {

                $statusBox.find('p').text(resp.content);

                if(resp.status === true) {
                    $statusBox.addClass('success');
                    $('#'+id).remove();
                }
                else {
                    $statusBox.addClass('error');
                }

                $statusBox.fadeIn(1200);
                $statusBox.fadeOut(1200);
            });
        },
        init: function () {
            this.$delete.on('click', this.onDelete);
        }
    };
    deleteFtr.init();


    var photoSel = {
        $photoElm: $('.highlight'),
        $stagedImg: $('.staged_img'),
        $effectBtns: $('.effects_button'),
        $default_text: $('.default_text'),
        loadPhotoInCanvas: function (event) {
            event.preventDefault();
            var $this = $(this);
            effectFtr.$loader.removeClass('hide');
            var src = $this.find('img').attr('src');
            photoSel.$stagedImg.hide().attr('src', src).fadeIn(1200);
            effectFtr.$loader.addClass('hide');
            photoSel.$effectBtns.fadeIn(1200);
            if(!$this.hasClass('on-display')) {
                // deactivate others
                $('.on-display').addClass('highlight').removeClass('on-display');
                photoSel.$default_text.addClass('hide');

                $this.removeClass('highlight').addClass('on-display');
            }
        },
        init: function () {
            this.$photoElm.on('click', this.loadPhotoInCanvas);
        }
    };
    photoSel.init();

    var effectFtr = {
        $effectBtn: $('.effect-btn'),
        $loader: $('.loader'),
        applyEffect: function (event) {
            event.preventDefault();
            var $this = $(this);
            if(!$this.hasClass('disabled')) {
                $('.effect-btn.disabled').removeClass('disabled');
                $this.addClass('disabled');
                var effect = $this.data('effect');
                var url = $this.data('url');
                var photoId = $('.on-display').attr('id');
                var index = photoId.split('-')[1];
                url = url + '?photo=' + index + '&effect=' + effect;
                effectFtr.$loader.removeClass('hide');
                
                $.get(url).then(
                    function (resp) {
                        var src = resp.staged_photo;
                        photoSel.$stagedImg.attr('src', src);
                        $('.loader').addClass('hide');
                    },
                    function () {

                    },
                    function () {

                    }
                );

                
            }


        },

        init: function () {
            this.$effectBtn.on('click', this.applyEffect);
        }
    };

    effectFtr.init();
});