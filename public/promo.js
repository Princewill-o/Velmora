export const campaign={name:'Black Friday',discount:.2,ids:['VLM-002','VLM-003','VLM-008','VLM-010','VLM-024','VLM-028','VLM-041','VLM-048']};
export function onSale(p){return campaign.ids.includes(p.id);}
export function salePrice(p){return onSale(p)?Math.round(p.price_gbp*(1-campaign.discount)*100)/100:p.price_gbp;}
export function saving(p){return p.price_gbp-salePrice(p);}
