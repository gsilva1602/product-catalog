const catalog = require('./catalog.json')
const catalogo = require('./catalogo.json')

console.log('catalogo', catalogo)
console.log('catalog', catalog)

const typedProductCatalog = 'laranja'
const containsCatalog = catalog.A.product
console.log(containsCatalog, typedProductCatalog)

if(typedProductCatalog.toLowerCase() === containsCatalog.toLowerCase()) {
    console.log('equal Catalog')
}

const typedProductCatalogo = 'limao' // must be exactly the same as stored
const containsCatalogo = catalogo.B
console.log(typedProductCatalogo, containsCatalogo)

if(containsCatalogo.includes(typedProductCatalogo)) {
    console.log('equal Catalogo')
}

// if not equal as stored, this is needed:
containsCatalogo.forEach(element => { // the forEach access each element and read it.
    const containsCatalogoToLowerCase = element.toString().toLowerCase()
    if(containsCatalogoToLowerCase === typedProductCatalogo.toLowerCase()) {
        console.log('equal Catalogo not the same stored');
    }
});