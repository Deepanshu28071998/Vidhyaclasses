const banners = [
    "Navratri_Banner.jpg",
    "355167888_753795866749007_8134489539911786255_n.jpg",
    "Ganesh_Chaturti_Banner.jpg",
    "VC_Banner12.jpg"
];

let currentIndex = 0;

function showBanner(index) {
    const banner = document.getElementById('banner');
    banner.src = banners[index];
}

function nextBanner() {
    currentIndex = (currentIndex + 1) % banners.length;
    showBanner(currentIndex);
}

function prevBanner() {
    currentIndex = (currentIndex - 1 + banners.length) % banners.length;
    showBanner(currentIndex);
}

// Automatic banner swap every 5 seconds
setInterval(nextBanner, 5000);

// Initial banner display
showBanner(currentIndex);

// const toppers = [
//     "https://media.gettyimages.com/id/517876430/photo/late-teen-happy-girl-students-studying-a-book-together.jpg?s=612x612&w=gi&k=20&c=Ve56aAzmqrYVAernvpahhCMqJuG2-mitv8iHwIXgAWo=",
//     "https://www.shutterstock.com/image-photo/young-male-college-student-wearing-260nw-2287978891.jpg",
//     "https://media.gettyimages.com/id/1049281412/photo/cute-schoolgirl-smiling-balancing-stack-of-books-on-the-head-at-library.jpg?s=612x612&w=gi&k=20&c=VKZHo8rHkRKMmvhwYBR3XALnalCuqcI4l1KHUdLkTs4=",
//     "https://plus.unsplash.com/premium_photo-1681681082157-b7b3d3e8d4f5?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8c3R1ZGVudCUyMHdpdGglMjBib29rc3xlbnwwfHwwfHx8MA%3D%3D",
//     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQfZZ_FCqzjw4r1kXpX0k5RnhxIyvFHfAyPA&s",
//     "https://png.pngtree.com/thumb_back/fh260/background/20231220/pngtree-primary-school-students-learn-to-read-books-photo-image_15528457.png"
// ];
let currentIndex2 = 0;
const totalImages = document.querySelectorAll('.image-frame img').length;
const imagePerFrame = 4;
const frame = document.querySelector('.image-frame');
const totalFrames = Math.ceil(totalImages / imagePerFrame);

function updateFramePosition(){
    frame.style.transform = `translateX(${-currentIndex2 * 100}%)`;
}

function nextImage(){
    currentIndex2 = (currentIndex2 + 1) % totalFrames;
    updateFramePosition();
}

function prevImage(){
    currentIndex2 = (currentIndex2 - 1 + totalFrames) % totalFrames;
    updateFramePosition();
}

let autoSwap = setInterval(nextImage, 5000);

document.querySelector('.prev').addEventListener('click', function(){
    clearInterval(autoSwap);
    autoSwap = setInterval(nextImage, 5000);
});
document.querySelector('next').addEventListener('click', function(){
    clearInterval(autoSwap);
    autoSwap = setInterval(nextImage, 5000);
});
