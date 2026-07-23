import { getCollection } from 'astro:content';

/** getStaticPaths partagé par les 3 variantes de langue de la fiche détail. */
export async function getAssetStaticPaths() {
  const assets = (await getCollection('assets')).filter((a) => !a.data.draft);
  return assets.map((a) => ({ params: { slug: a.id }, props: { asset: a } }));
}
