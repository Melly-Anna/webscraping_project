
LDLC
UPDATE phones_ldlc
SET categorie = CASE
    WHEN nom LIKE '%iPhone 13%' THEN 'iPhone 13'
    WHEN nom LIKE '%iPhone 14%' AND nom NOT LIKE '%Plus%' AND nom NOT LIKE '%Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 14'
    WHEN nom LIKE '%iPhone 14 Plus%' THEN 'iPhone 14 Plus'
    WHEN nom LIKE '%iPhone 14 Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 14 Pro'
    WHEN nom LIKE '%iPhone 14 Pro Max%' THEN 'iPhone 14 Pro Max'
    WHEN nom LIKE '%iPhone 15%' AND nom NOT LIKE '%Plus%' AND nom NOT LIKE '%Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 15'
    WHEN nom LIKE '%iPhone 15 Plus%' THEN 'iPhone 15 Plus'
    WHEN nom LIKE '%iPhone 15 Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 15 Pro'
    WHEN nom LIKE '%iPhone 15 Pro Max%' THEN 'iPhone 15 Pro Max'
    WHEN nom LIKE '%iPhone 16%' AND nom NOT LIKE '%Plus%' AND nom NOT LIKE '%Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 16'
    WHEN nom LIKE '%iPhone 16 Plus%' THEN 'iPhone 16 Plus'
    WHEN nom LIKE '%iPhone 16 Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 16 Pro'
    WHEN nom LIKE '%iPhone 16 Pro Max%' THEN 'iPhone 16 Pro Max'
    ELSE 'Autre'
END;

UPDATE phones_ldlc
SET stockage = CASE
    WHEN nom LIKE '%128 Go%' THEN '128 Go'
    WHEN nom LIKE '%256 Go%' THEN '256 Go'
    WHEN nom LIKE '%512 Go%' THEN '512 Go'
    WHEN nom LIKE '%1 To%' THEN '1 To'
    ELSE 'Inconnu' 
END;



MOBILE SHOP 
UPDATE phones_mobileshop
SET categorie = CASE
    WHEN nom LIKE '%iPhone 13%' THEN 'iPhone 13'
    WHEN nom LIKE '%iPhone 14%' AND nom NOT LIKE '%Plus%' AND nom NOT LIKE '%Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 14'
    WHEN nom LIKE '%iPhone 14 Plus%' THEN 'iPhone 14 Plus'
    WHEN nom LIKE '%iPhone 14 Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 14 Pro'
    WHEN nom LIKE '%iPhone 14 Pro Max%' THEN 'iPhone 14 Pro Max'
    WHEN nom LIKE '%iPhone 15%' AND nom NOT LIKE '%Plus%' AND nom NOT LIKE '%Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 15'
    WHEN nom LIKE '%iPhone 15 Plus%' THEN 'iPhone 15 Plus'
    WHEN nom LIKE '%iPhone 15 Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 15 Pro'
    WHEN nom LIKE '%iPhone 15 Pro Max%' THEN 'iPhone 15 Pro Max'
    WHEN nom LIKE '%iPhone 16%' AND nom NOT LIKE '%Plus%' AND nom NOT LIKE '%Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 16'
    WHEN nom LIKE '%iPhone 16 Plus%' THEN 'iPhone 16 Plus'
    WHEN nom LIKE '%iPhone 16 Pro%' AND nom NOT LIKE '%Pro Max%' THEN 'iPhone 16 Pro'
    WHEN nom LIKE '%iPhone 16 Pro Max%' THEN 'iPhone 16 Pro Max'
    ELSE 'Autre'
END;

UPDATE phones_mobileshop
SET stockage = CASE
    WHEN nom LIKE '%128GB%' THEN '128 Go'
    WHEN nom LIKE '%256GB%' THEN '256 Go'
    WHEN nom LIKE '%512GB%' THEN '512 Go'
    WHEN nom LIKE '%1TB%' THEN '1 To'
    ELSE 'Inconnu' 
END;