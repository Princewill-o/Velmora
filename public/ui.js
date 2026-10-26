export function icon(){return `<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 7h14l1 14H4L5 7Z"/><path d="M8 8V6a4 4 0 0 1 8 0v2"/></svg>`;}
export const palette={pewter:'#777777',ivory:'#e6d9be',midnight:'#292d40',champagne:'#b89b73',emerald:'#285047',black:'#292729',sapphire:'#344e70',oxblood:'#6b1f2a',burgundy:'#6b1f2a',navy:'#29344c',silver:'#969491',gold:'#ad8c54',rose:'#ae7c76','dusty rose':'#b18985',chocolate:'#594139'};
export function garment(p,colour=p.colours[0]){

 const kind=p.name.toLowerCase().includes('scarf')?'scarf':p.category==='dress'?(p.fit==='wrap'?'dress-wrap':['structured','A-line'].includes(p.fit)?'dress-structured':'dress'):p.category;
 const asset=`/assets/garment-${kind}.webp`,tint=palette[colour]||'#777064';
 return `<div class="garment-render category-${p.category}" style="--garment-tint:${tint};--garment-image:url('${asset}')"><img src="${asset}" alt="Digital ${p.category} concept in ${colour}; illustrative, not verified product photography" loading="lazy" decoding="async"><span class="garment-tint" aria-hidden="true"></span></div>`;
}
