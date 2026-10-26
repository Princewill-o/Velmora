import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {Window} from 'happy-dom';

test('sale collection, product choices and bag use the same discounted price',async()=>{
 const page=new Window({url:'http://localhost:4187/#/collection?sale=1',settings:{disableCSSFileLoading:true,disableJavaScriptFileLoading:true,disableComputedStyleRendering:true}});
 page.document.write(await readFile(new URL('../public/index.html',import.meta.url),'utf8'));
 const products=JSON.parse(await readFile(new URL('../public/products.json',import.meta.url)));
 const keys=['window','document','location','localStorage','FormData','IntersectionObserver','ResizeObserver','matchMedia','requestAnimationFrame','cancelAnimationFrame'];
 const previous=new Map(keys.map(k=>[k,globalThis[k]]));const oldFetch=globalThis.fetch;
 for(const k of keys)globalThis[k]=typeof page[k]==='function'&&['matchMedia','requestAnimationFrame','cancelAnimationFrame'].includes(k)?page[k].bind(page):page[k];
 globalThis.window=page;page.scrollTo=()=>{};page.HTMLElement.prototype.scrollIntoView=()=>{};page.HTMLDialogElement.prototype.showModal=function(){this.open=true;};page.HTMLDialogElement.prototype.close=function(){this.open=false;};
 globalThis.fetch=async()=>({ok:true,json:async()=>products});
 try{
  await import('../public/app.js');
  const d=page.document;
  assert.equal(d.querySelectorAll('#collection-results .product-card').length,8);
  const card=d.querySelector('[href="#/product/VLM-003"]');assert.match(card.textContent,/£248/);assert.match(card.textContent,/£310/);
  page.location.hash='#/product/VLM-003';page.dispatchEvent(new page.Event('hashchange'));
  assert.equal(d.querySelector('.price .sale-price').textContent,'£248');
  d.querySelector('#add-bag').click();assert.match(d.querySelector('#size-error').textContent,/Choose a size/);assert.equal(d.querySelector('#bag').open,false);
  d.querySelector('[data-size="UK 10"]').click();d.querySelector('[data-colour="emerald"]').click();d.querySelector('#add-bag').click();
  assert.equal(d.querySelector('#bag').open,true);assert.match(d.querySelector('.bag-line').textContent,/UK 10 · emerald/);assert.match(d.querySelector('.bag-total').textContent,/£248/);assert.match(d.querySelector('.bag-savings').textContent,/£62/);
  d.querySelector('[data-delta="1"]').click();assert.match(d.querySelector('.bag-total').textContent,/£496/);assert.match(d.querySelector('.bag-savings').textContent,/£124/);
  assert.deepEqual(JSON.parse(page.localStorage.getItem('velmora-bag')),[{id:'VLM-003',size:'UK 10',colour:'emerald',quantity:2}]);
  d.querySelector('[data-remove]').click();assert.match(d.querySelector('#bag-content').textContent,/An evening awaits/);
  page.location.hash='#/';page.dispatchEvent(new page.Event('hashchange'));
  assert.equal(d.querySelectorAll('[data-scene]').length,2);assert.match(d.querySelector('main').textContent,/20% OFF|20% off selected/);
  page.location.hash='#/atelier';page.dispatchEvent(new page.Event('hashchange'));
  assert.equal(d.querySelectorAll('[data-fabric]').length,3);assert.ok(d.querySelector('[data-motion-action="left"]'));assert.match(d.querySelector('main').textContent,/not exact catalogue garments/);
 }finally{
  // Wait for the lazily imported module before disposing the emulated DOM.
  await new Promise(resolve=>setTimeout(resolve,50));page.happyDOM.abort();page.happyDOM.close();globalThis.fetch=oldFetch;for(const [k,v] of previous){if(v===undefined)delete globalThis[k];else globalThis[k]=v;}
 }
});
