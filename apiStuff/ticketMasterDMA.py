# Convert the DMA data into a dictionary where the key is the name and the value is the DMA ID.
dma_data = """
DMA ID	DMA name
200	All of US
212	Abilene - Sweetwater
213	Albany - Schenectady - Troy
214	Albany, GA
215	Albuquerque - Santa Fe
216	Alexandria, LA
217	Alpena
218	Amarillo
219	Anchorage
220	Atlanta
221	Augusta
222	Austin
223	Bakersfield
224	Baltimore
225	Bangor
226	Baton Rouge
227	Beaumont - Port Arthur
228	Bend, OR
229	Billings
230	Biloxi - Gulfport
231	Binghamton
232	Birmingham (Anniston and Tuscaloosa)
233	Bluefield - Beckley - Oak Hill
234	Boise
235	Boston (Manchester)
236	Bowling Green
237	Buffalo
238	Burlington - Plattsburgh
239	Butte - Bozeman
240	Casper - Riverton
241	Cedar Rapids - Waterloo & Dubuque
242	Champaign & Springfield - Decatur
243	Charleston, SC
244	Charleston-Huntington
245	Charlotte
246	Charlottesville
247	Chattanooga
248	Cheyenne - Scottsbluff
249	Chicago
250	Chico - Redding
251	Cincinnati
252	Clarksburg - Weston
253	Cleveland
254	Colorado Springs - Pueblo
255	Columbia - Jefferson City
256	Columbia, SC
257	Columbus - Tupelo - West Point
258	Columbus, GA
259	Columbus, OH
260	Corpus Christi
261	Dallas - Fort Worth
262	Davenport - Rock Island - Moline
263	Dayton
264	Denver
265	Des Moines - Ames
266	Detroit
267	Dothan
268	Duluth - Superior
269	El Paso
270	Elmira
271	Erie
272	Eugene
273	Eureka
274	Evansville
275	Fairbanks
276	Fargo - Valley City
277	Flint - Saginaw - Bay City
278	Florence - Myrtle Beach
279	Fort Myers - Naples
280	Fort Smith - Fayetteville - Springdale - Rogers
281	Fort Wayne
282	Fresno - Visalia
283	Gainesville
284	Glendive
285	Grand Junction - Montrose
286	Grand Rapids - Kalamazoo - Battle Creek
287	Great Falls
288	Green Bay - Appleton
289	Greensboro - High Point - Winston-Salem
290	Greenville - New Bern - Washington
291	Greenville - Spartansburg - Asheville - Anderson
292	Greenwood - Greenville
293	Harlingen - Weslaco - Brownsville - McAllen
294	Harrisburg - Lancaster - Lebanon - York
295	Harrisonburg
296	Hartford & New Haven
297	Hattiesburg - Laurel
298	Helena
299	Honolulu
300	Houston
301	Huntsville - Decatur (Florence)
302	Idaho Falls - Pocatello
303	Indianapolis
304	Jackson, MS
305	Jackson, TN
306	Jacksonville
307	Johnstown - Altoona
308	Jonesboro
309	Joplin - Pittsburg
310	Juneau
311	Kansas City
312	Knoxville
313	La Crosse - Eau Claire
314	Lafayette, IN
315	Lafayette, LA
316	Lake Charles
317	Lansing
318	Laredo
319	Las Vegas
320	Lexington
321	Lima
322	Lincoln & Hastings - Kearney
323	Little Rock - Pine Bluff
324	Los Angeles
325	Louisville
326	Lubbock
327	Macon
328	Madison
329	Mankato
330	Marquette
331	Medford - Klamath Falls
332	Memphis
333	Meridian
334	Miami - Fort Lauderdale
335	Milwaukee
336	Minneapolis - Saint Paul
337	Minot - Bismarck - Dickinson
338	Missoula
339	Mobile - Pensacola (Fort Walton Beach)
340	Monroe - El Dorado
341	Monterey - Salinas
342	Montgomery (Selma)
343	Nashville
344	New Orleans
345	New York
346	Norfolk - Portsmouth - Newport News
347	North Platte
348	Odessa - Midland
349	Oklahoma City
350	Omaha
351	Orlando - Daytona Beach - Melbourne
352	Ottumwa - Kirksville
353	Paducah - Cape Girardeau - Harrisburg - Mt Vernon
354	Palm Springs
355	Panama City
356	Parkersburg
357	Peoria - Bloomington
358	Philadelphia
359	Phoenix
360	Pittsburgh
361	Portland - Auburn
362	Portland, OR
363	Presque Isle
364	Providence - New Bedford
365	Quincy - Hannibal - Keokuk
366	Raleigh - Durham (Fayetteville)
367	Rapid City
368	Reno
369	Richmond - Petersburg
370	Roanoke - Lynchburg
371	Rochester - Mason City - Austin
372	Rochester, NY
373	Rockford
374	Sacramento - Stockton - Modesto
375	Saint Joseph
376	Saint Louis
377	Salisbury
378	Salt Lake City
379	San Angelo
380	San Antonio
381	San Diego
382	San Francisco - Oakland - San Jose
383	Santa Barbara - Santa Maria - San Luis Obispo
384	Savannah
385	Seattle - Tacoma
386	Sherman - Ada
387	Shreveport
388	Sioux City
389	Sioux Falls (Mitchell)
390	South Bend - Elkhart
391	Spokane
392	Springfield - Holyoke
393	Springfield, MO
394	Syracuse
395	Tallahassee - Thomasville
396	Tampa - Saint Petersburg (Sarasota)
397	Terre Haute
398	Toledo
399	Topeka
400	Traverse City - Cadillac
401	Tri-Cities, TN-VA
402	Tucson (Sierra Vista)
403	Tulsa
404	Twin Falls
405	Tyler - Longview (Lufkin & Nacogdoches)
406	Utica
407	Victoria
408	Waco - Temple - Bryan
409	Washington DC (Hagerstown)
410	Watertown
411	Wausau - Rhinelander
412	West Palm Beach - Fort Pierce
413	Wheeling - Steubenville
414	Wichita - Hutchinson
415	Wichita Falls & Lawton
416	Wilkes Barre - Scranton
417	Wilmington
418	Yakima - Pasco - Richland - Kennewick
419	Youngstown
420	Yuma - El Centro
421	Zanesville
422	Northern New Jersey
500	All of Canada
501	Barrie-Orillia
502	Belleville-Peterborough
503	Owen Sound
504	Burnaby-New Westminster-Surrey
505	Calgary-Banff
506	Edmonton
507	Fraser Valley
508	Hamilton-Niagara
509	Kitchener-Waterloo
510	London-Sarnia
511	Mississauga-Oakville
512	Newfoundland
513	NWT
514	New Brunswick
515	Northern Ontario
516	Nova Scotia
517	Nunavit
518	Okanagan-Kootenays
519	Ottawa-Gatineau
520	PEI
521	Prince George-North
522	Montreal and Surrounding Area
523	Red Deer
524	Saskatchewan
527	Toronto
528	Vancouver
529	Sunshine Coast-Islands
530	Winnipeg-Brandon
531	Yukon
601	All of United Kingdom
602	London
603	South
604	Midlands and Central
605	Wales and North West
606	North and North East
607	Scotland
608	All of Ireland
609	Northern Ireland
610	Germany
611	Netherlands
612	Sweden
613	Turkey
701	All of Australia
702	New South Wales/Australian Capital Territory
703	Queensland
704	Western Australia
705	Victoria/Tasmania
750	All of New Zealand
751	North Island
752	South Island
801	All of Mexico
802	Mexico City and Metropolitan Area
803	Monterrey
804	Guadalajara
901	All of Spain
902	Barcelona
903	Madrid
"""

# Parse the data into a dictionary
lines = dma_data.strip().split('\n')[1:]  # Skip the header
dma_dict = {}

for line in lines:
    dma_id, dma_name = line.split('\t')
    dma_dict[dma_name] = dma_id

dma_dict

#create a list of the keys
def get_cities(dma_dict = dma_dict):
    return list(dma_dict.keys())

#create a list of the values
def get_values(dma_dict):
    return list(dma_dict.values())

#given a city, return the value 
def get_value(dma_dict, key):
    return dma_dict[key]


#test the functions
# print(get_cities(dma_dict))
# # print(get_values(dma_dict))

print( get_cities())

