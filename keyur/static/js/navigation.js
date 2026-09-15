window.getSelectedProductSize = function (productElement) {
  const sizeSelect = productElement?.querySelector('.product-size, select');
  return sizeSelect ? sizeSelect.value : '';
};

document.addEventListener('DOMContentLoaded', function () {
  const path = window.location.pathname.replace(/\/$/, '');
  const links = document.querySelectorAll('.navbar a.nav-link');

  links.forEach(function (link) {
    const href = link.getAttribute('href') || '';
    const linkPath = new URL(href, window.location.origin).pathname.replace(/\/$/, '');
    const isHome = (path === '' || path.endsWith('/frontend')) && linkPath.endsWith('/frontend');
    const isShop = (path.endsWith('/shop') || path.includes('/product')) && linkPath.endsWith('/shop');
    const isOrders = path.includes('/orders') && linkPath.endsWith('/orders');
    const isProfile = path.endsWith('/user') && linkPath.endsWith('/user');
    const isCart = path.endsWith('/cart') && linkPath.endsWith('/cart');

    if (isHome || isShop || isOrders || isProfile || isCart) {
      link.classList.add('active');
      link.closest('.nav-item')?.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });

  document.querySelectorAll('.sproduct').forEach(function (product) {
    let sizeSelect = product.querySelector('.product-size, select');
    if (!sizeSelect) {
      sizeSelect = document.createElement('select');
      sizeSelect.className = 'form-control product-size mb-2';
      sizeSelect.innerHTML = '<option value="">Select Size</option><option value="S">S</option><option value="M">M</option><option value="L">L</option><option value="XL">XL</option><option value="XXL">XXL</option>';
      product.appendChild(sizeSelect);
    }
    sizeSelect.required = true;
    sizeSelect.addEventListener('click', function (event) {
      event.stopPropagation();
    });
  });

  document.addEventListener('click', function (event) {
    const button = event.target.closest('.buy-btn, .btn-danger, .btn-success');
    if (!button) return;
    const product = button.closest('.sproduct');
    const sizeSelect = product?.querySelector('.product-size, select');
    if (!sizeSelect) return;
    if (!sizeSelect.value) {
      event.preventDefault();
      event.stopImmediatePropagation();
      sizeSelect.focus();
      alert('Please select a size before continuing.');
      return;
    }

    setTimeout(function () {
      const storageKey = Object.keys(localStorage).find(function (key) {
        return key.indexOf('cart_') === 0 && !key.endsWith('_checkout');
      }) || 'cart_guest';
      const cart = JSON.parse(localStorage.getItem(storageKey) || '[]');
      const productName = product.querySelector('h3, .p-name')?.textContent.trim();
      const cartItem = cart.find(function (item) {
        return !item.size && (!productName || item.name === productName);
      }) || cart[cart.length - 1];
      if (cartItem && !cartItem.size) {
        cartItem.size = sizeSelect.value;
        localStorage.setItem(storageKey, JSON.stringify(cart));
      }
    }, 0);
  }, true);
});
