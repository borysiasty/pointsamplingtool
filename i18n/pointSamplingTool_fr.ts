<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS><TS version="2.0" language="fr_FR" sourcelanguage="">
<context>
    <name>Dialog</name>
    <message>
        <location filename="../doPointSamplingTool.py" line="336"/>
        <source>Point Sampling Tool</source>
        <translation>Point Sampling Tool</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="34"/>
        <source>General</source>
        <translation>Général</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="48"/>
        <source>Layer containing sampling points:</source>
        <translation>Couche vecteur contenant les points :</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="68"/>
        <source>Layers with fields/bands to get values from:</source>
        <translation>Couches avec les champs/bandes d&apos;où extraire les valeurs :</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="99"/>
        <source>Output point vector layer:</source>
        <translation>Couche de points en sortie</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="110"/>
        <source>Browse</source>
        <translation>Naviguer</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="119"/>
        <source>Add created layer to the map</source>
        <translation>Ajouter la couche créée à la carte</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="130"/>
        <source>Fields</source>
        <translation>Champs</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="167"/>
        <source>source</source>
        <translation>source</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="172"/>
        <source>name</source>
        <translation>nom</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="181"/>
        <source>About</source>
        <translation>A propos</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="190"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;The Point Sampling Tool Plugin collects polygon attributes and raster values from multiple layers at specified sampling points. You need a point layer with locations of sampling points and at least one polygon or raster layer to probe values from. The plugin creates a new point layer with locations given by the sampling points and attributes taken from all the underlying polygons or/and raster cells.&lt;/p&gt;&lt;p&gt;Please use Control and Shift keys in order to select multiple columns and bands.&lt;/p&gt;&lt;p&gt;NOTE: This tool is not compatible with mulitipoint sources, unless each multipoint contains exactly one point. Using multipoint samples that contain more points in multipoints may produce unreliable results.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Point Sampling Tool Plugin récupère les valeurs de polygones ou de pixels d&apos;un raster situé sous un échantillon de points. Une couche de points est nécessaire avec la localisation des points ainsi d&apos;une couche de polygones ou un raster d&apos;où récupérer les valeurs. Le plugin crée une nouvelle couche de points avec la localisation de la couche de points en entrée et les attributs récupérés de toutes les couches sélectionnées (polygones ou raster).&lt;/p&gt;&lt;p&gt;Veuillez utiliser les touches Ctrl et Shift pour sélectionner plusieurs champs ou bandes.&lt;/p&gt;&lt;p&gt;NOTE: Cet outil n&apos;est pas compatible avec les couches multipoints, à moins que chacun n&apos;en contiennent qu&apos;un. Utiliser une couche multipoints avec plusieurs points par entité ne renvoie pas de résultats appropriés.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="233"/>
        <source>Status:</source>
        <translation>Status:</translation>
    </message>
    <message>
        <location filename="../pointSamplingToolUi.ui" line="260"/>
        <source>Complete the input fields and press OK...</source>
        <translation>Compléter les entrées et appuyer sur OK</translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="203"/>
        <source>Name length can&apos;t exceed 10 chars, so it has been truncated.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="218"/>
        <source>Output file</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="218"/>
        <source>GeoPackages(*.gpkg);;Comma separated values (*.csv);;Shapefiles (*.shp)</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="232"/>
        <source>Check input values, please!</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="245"/>
        <source>Please select vector layer containing the sampling points</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="249"/>
        <source>Please select at least one polygon attribute or raster band</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="253"/>
        <source>Please specify output file name</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="259"/>
        <source>At least two field names are the same!
Please type unique names.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="265"/>
        <source>&lt;html&gt;All layers must have the same coordinate refere system. The &lt;b&gt;%s&lt;/b&gt; layer seems to have different CRS id (&lt;b&gt;%d&lt;/b&gt;)
                   than the point layer (&lt;b&gt;%d&lt;/b&gt;). If they are two different CRSes, you need to reproject one of the layers first,
                   otherwise results will be wrong.&lt;br/&gt;
                   However, if you are sure both CRSes are the same, and they are just improperly recognized, you can safely continue.
                   Do you want to continue?&lt;/html&gt;</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="282"/>
        <source>Point Sampling Tool: layer CRS mismatch!</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="287"/>
        <source>Processing the output file name...</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="298"/>
        <source>File %s already exists. Do you want to overwrite?</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="311"/>
        <source>Fill up the input fields, please.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="305"/>
        <source>Please provide &lt;b&gt;table name&lt;/b&gt; for your layer.&lt;br/&gt;
                      &lt;b&gt;WARNING: &lt;/b&gt;Database %s already exists. If you select a table existing in it, the table will be overwritten.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="314"/>
        <source>Processing...</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="333"/>
        <source>OK. The new layer has been added to the map.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="335"/>
        <source>Error loading the created layer</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="336"/>
        <source>The new layer seems to be created, but is invalid.
It won&apos;t be loaded.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="368"/>
        <source>Writing data to the new layer...</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="377"/>
        <source>Processing point %s of %s</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="450"/>
        <source>Point sampling tool</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../doPointSamplingTool.py" line="454"/>
        <source>The new layer has been created.</source>
        <translation type="unfinished"></translation>
    </message>
</context>
<context>
    <name>Point Sampling Tool</name>
    <message>
        <location filename="../pointSamplingTool.py" line="54"/>
        <source>Point Sampling Tool</source>
        <translation type="unfinished">Point Sampling Tool</translation>
    </message>
    <message>
        <location filename="../pointSamplingTool.py" line="57"/>
        <source>Collects polygon attributes and raster values from multiple layers at specified sampling points</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../pointSamplingTool.py" line="67"/>
        <source>&amp;Analyses</source>
        <translation type="unfinished"></translation>
    </message>
</context>
</TS>
